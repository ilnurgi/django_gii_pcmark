"""
админка для тестов
"""

from django.contrib import admin

from django_gii_pcmark.models.marks import Mark


class MarkAdmin(admin.ModelAdmin):
    """
    админка для теста
    """
    list_display = ('system', 'test_soft', 'val_min', 'val_avg', 'val_max', 'test_quality')

    fieldsets = (
        (
            'Стенд и окружение',
            {
                'fields': (
                    ('system', 'screen_size'),
                    ('test_soft', 'test_soft_version', 'os', 'gpu_driver', 'test_quality'),
                    'url',
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
        (
            'Доп параметры',
            {
                'fields': (
                    (
                        'overclock_cpu_freq',
                        'overclock_ram_freq',
                    ),
                    (
                        'gpu_producer',
                        'gpu_model',
                        'overclock_gpu_core_freq',
                        'overclock_gpu_ram_freq',
                    ),
                    'comments',
                ),
                'classes': ('collapse',),
            }
        )
    )


admin.site.register(Mark, MarkAdmin)
