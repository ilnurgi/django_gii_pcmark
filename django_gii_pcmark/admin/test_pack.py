"""
настройка админки по тест пакам
"""

from django.contrib import admin
from django.db import connection

from django_gii_pcmark.models.hardware import CPU, VideoCard, MotherBoard
from django_gii_pcmark.models.marks import Mark, TestPack


class MBFilter(admin.SimpleListFilter):
    """
    фильтр по материнским платам
    """
    title = 'mb'
    parameter_name = 'mb'

    def lookups(self, request, model_admin):
        """
        возвращаем варианты для клиента
        :param request:
        :param model_admin:
        :return:
        """
        return [
            (mb['id'], '{0} {1} ({2}) '.format(mb['producer__name'], mb['model'], mb['socket__name']))
            for mb in MotherBoard.objects
                .all()
                .order_by('producer__name', 'model', 'socket__name')
                .values('producer__name', 'socket__name', 'model', 'id')
        ]

    def queryset(self, request, queryset):
        """
        фильтруем элементы списка
        :param request:
        :param queryset:
        :return:
        """
        value = self.value()
        if value:
            return queryset.filter(system__mother_board=value)


class CPUFilter(admin.SimpleListFilter):
    """
    фильтр по процессорам
    """
    title = 'cpu'
    parameter_name = 'cpu'

    def lookups(self, request, model_admin):
        """
        возвращаем варианты для клиента
        :param request:
        :param model_admin:
        :return:
        """
        if request.GET.get('mb'):
            with connection.cursor() as cursor:
                cursor.execute(
                    '''
                    select
                      t_producer.name producer__name
                      , t_cpu.model model
                      , t_series.name series__name
                      , t_cpu.id 
                    from 
                      django_gii_pcmark_cpu t_cpu
                      inner join
                        django_gii_pcmark_producersdict t_producer 
                        on 
                          t_cpu.producer_id = t_producer.id
                      inner join 
                        django_gii_pcmark_processorseriesdict t_series 
                        on 
                          t_cpu.series_id = t_series.id
                    where 
                      t_cpu.id in (                    
                        select
                          distinct t_system.cpu_id
                        from
                          django_gii_pcmark_system t_system
                        where 
                          t_system.mother_board_id = any(%s::int[])
                      )
                    order by 
                        t_producer.name, t_cpu.model
                    ''',
                    [
                        '{{{0}}}'.format(','.join(request.GET['mb']))
                    ]
                )
                data = cursor.fetchall()
                columns = [d.name for d in cursor.description]
                cpu_objects = (dict(zip(columns, row)) for row in data)
        else:
            cpu_objects = (
                CPU.objects
                    .all()
                    .order_by('producer__name', 'series__name', 'model')
                    .values('producer__name', 'series__name', 'model', 'id')
            )
        return [
            (cpu['id'], '{0} {1} ({2})'.format(cpu['producer__name'], cpu['series__name'], cpu['model']))
            for cpu in cpu_objects
        ]

    def queryset(self, request, queryset):
        """
        фильтруем элементы списка
        :param request:
        :param queryset:
        :return:
        """
        value = self.value()
        if value:
            return queryset.filter(system__cpu=value)


class VideoCardFilter(admin.SimpleListFilter):
    """
    фильтр по видео картам
    """
    title = 'vc'
    parameter_name = 'vc'

    def lookups(self, request, model_admin):
        """
        возвращаем варианты для клиента
        :param request:
        :param model_admin:
        :return:
        """
        print(request.GET)
        if request.GET.get('mb') or request.GET.get('cpu'):
            with connection.cursor() as cursor:
                cursor.execute(
                    '''
                    select
                      t_vc.model
                    from 
                      django_gii_pcmark_videocard t_vc
                      inner join
                        django_gii_pcmark_producersdict t_producer 
                        on 
                          t_vc.producer_id = t_producer.id
                    where 
                      t_vc.id in (                    
                        select
                          distinct t_system.video_card_id
                        from
                          django_gii_pcmark_system t_system
                        where 
                          (
                            %(mb)s::int[] is null
                            or t_system.mother_board_id = any(%(mb)s::int[])
                          )
                          and
                          (
                            %(cpu)s::int[] is null
                            or t_system.cpu_id = any(%(cpu)s::int[])
                          )                          
                      )
                    order by 
                        t_producer.name, t_vc.model
                    ''',
                    {
                        'mb': '{{{0}}}'.format(','.join(request.GET.get('mb'))) if request.GET.get('mb') else None,
                        'cpu': '{{{0}}}'.format(','.join(request.GET.get('cpu'))) if request.GET.get('cpu') else None,
                    }
                )
                data = cursor.fetchall()
                columns = [d.name for d in cursor.description]
                vc_objects = (dict(zip(columns, row)) for row in data)
        else:
            vc_objects = (
                VideoCard.objects
                    .all()
                    .order_by('producer__name', 'model')
                    .distinct('producer__name', 'model')
                    .values('model')
            )
        return [(vc['model'], vc['model']) for vc in vc_objects]

    def queryset(self, request, queryset):
        """
        фильтруем элементы списка
        :param request:
        :param queryset:
        :return:
        """
        value = self.value()
        if value:
            return queryset.filter(system__videocard__model=value)


class MarkInline(admin.StackedInline):
    """
    инлайн тесты систем
    """
    model = Mark
    extra = 15
    fieldsets = (
        (
            'Стенд и окружение',
            {
                'fields': (
                    ('test_soft', 'test_soft_version'),
                    ('test_quality', 'anti_aliasing_version', 'directx_version'),
                    'screen_size',
                    'comments',
                )
            }
        ),
        (
            'Показатели',
            {
                'fields': (
                    ('val_min', 'val_avg', 'val_max'),
                )
            }
        ),
    )
    ordering = (
        'test_soft__name',
        'test_soft__mode',
        'test_soft__dimension',
        'test_quality__name',
        'screen_size__width',
    )


@admin.register(TestPack)
class TestPackAdmin(admin.ModelAdmin):
    """
    админка для пачки тестов
    """
    save_as = True
    save_on_top = True
    fieldsets = (
        (
            'Система',
            {
                'fields': (
                    'system',
                )
            }
        ),
        (
            'Окружение',
            {
                'fields': (
                    ('url', 'screen_size'),
                    ('os', 'gpu_driver'),
                    (
                        'overclock_cpu_freq',
                        'overclock_ram_freq',
                        'overclock_gpu_core_freq',
                        'overclock_gpu_ram_freq',
                    )
                )
            }
        ),
    )
    list_filter = (
        MBFilter,
        CPUFilter,
        VideoCardFilter,
    )
    ordering = (
        'system__mother_board__producer__name',
        'system__mother_board__model',
        'system__cpu__producer__name',
        'system__cpu__series__name',
        'system__cpu__model',
        'system__video_card__producer__name',
        'system__video_card__model',
        'system__gpu_producer__name',
        'system__gpu_model',
        'screen_size__width',
        'screen_size__height',
    )
    inlines = [
        MarkInline
    ]
