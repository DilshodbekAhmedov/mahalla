from django.contrib import admin


from .models import Sector, Neighborhood, Citizen


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    pass


@admin.register(Neighborhood)
class SectorAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.user_type == 'sector_leader':
            queryset = queryset.filter(sector=request.user.sector)
        return queryset


    list_display = 'name', 'sector',
    search_fields = 'name',
    list_filter = 'sector',





@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.user_type == 'nighborhood_leader':
            queryset = queryset.filter(neighborhood=request.user.neighborhood)
        elif request.user.user_type == 'sector_leader':
            queryset = queryset.filter(neighborhood__sector=request.user.sector)

        return queryset

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "neighborhood" and request.user.user_type == 'nighborhood_leader':
            kwargs["queryset"] = Neighborhood.objects.filter(id=request.user.neighborhood_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = 'full_name', 'neighborhood', 'passport', "birthdate", 'gender',
    list_filter = 'neighborhood', 'gender', 'address', 'disabiltiy', 'abroad', 'womens_notebook', 'pensioner'
    search_fields = 'full_name',
