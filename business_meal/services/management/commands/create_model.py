import os

from django.core.management.templates import TemplateCommand


class Command(TemplateCommand):
    def add_arguments(self, parser):
        parser.add_argument("app_name", type=str, help="app name")
        parser.add_argument("model_name", type=str, help="model_name")

    def create_model(self):
        with open(f"{self.project_dict}/{self.app_name}/models.py", "a") as f:
            f.write(
                f"""
class {self.model_name}(models.Model):
    #relations

    #fields

    def __str__(self):
        return self.pk
"""
            )

    def register_admin(self):
        with open(f"{self.project_dict}/{self.app_name}/admin.py", "a") as f:
            f.write(
                f"""
@admin.register(models.{self.model_name})
class {self.model_name}Admin(admin.ModelAdmin):
    "Admin View for {self.model_name}"

"""
            )

    def create_view(self):
        with open(f"{self.project_dict}/{self.app_name}/views.py", "a") as f:
            f.write(
                f"""
class {self.model_name}ViewSet(viewsets.ModelViewSet):
    queryset = query = models.{self.model_name}.objects.all()
    serializer_class = serializers.{self.model_name}Serializer
    # filterset_class = filter.{self.model_name}Filter
    # search_fields = ['']
    # filterset_fields = ['']

"""
            )

    def create_serializer(self):
        with open(f"{self.project_dict}/{self.app_name}/serializers.py", "a") as f:
            f.write(
                f"""
class {self.model_name}Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.{self.model_name}
        fields = '__all__'



"""
            )

    def handle(self, *args, **options):
        self.app_name = options["app_name"]
        self.model_name = options["model_name"]
        project_name = "business_meal"
        self.project_dict = os.path.join(os.getcwd(), project_name)
        self.create_model()
        self.register_admin()
        self.create_view()
        self.create_serializer()
