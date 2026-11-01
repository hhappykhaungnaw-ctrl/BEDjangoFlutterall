from django.db import models

class Currency(models.Model):
    currency_id = models.AutoField(primary_key=True)
    currency_code = models.CharField(max_length=3)
    currency_name = models.CharField(max_length=50)
    currency_symbol = models.CharField(max_length=10, blank=True, null=True)
    decimal_places = models.IntegerField(default=2)
    is_functional_currency = models.BooleanField(default=False)
    is_presentation_currency = models.BooleanField(default=False)
    allow_transaction_currency = models.BooleanField(default=True)
    allow_exchange_rate_entry = models.BooleanField(default=True)
    amount_rounding_precision = models.DecimalField(max_digits=10, decimal_places=2, default=0.01)
    depreciation_rounding = models.DecimalField(max_digits=10, decimal_places=2, default=0.01)
    transaction_currency = models.CharField(max_length=3, blank=True, null=True)
    exchange_rate = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    functional_currency = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["currency_code"]

    def __str__(self):
        return f"{self.currency_code} - {self.currency_name}"
    

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    currency = models.ForeignKey(
        Currency,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="currency_id"
    )
    country_code = models.CharField(max_length=3)
    country_name = models.CharField(max_length=100)
    iso = models.CharField(max_length=3, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    default_time_zone = models.CharField(
        max_length=50, null=True, blank=True
    )
    default_language = models.CharField(
        max_length=20, null=True, blank=True
    )
    date_format = models.CharField(
        max_length=20, null=True, blank=True
    )
    allow_asset_location = models.BooleanField(default=True)
    default_country = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country_name

    class Meta:
        db_table = "country"


class Department(models.Model):

    class DepartmentType(models.TextChoices):
        HR = "HR", "HR"
        IT = "IT", "IT"
        FINANCE = "FINANCE", "FINANCE"
        SALES = "SALES", "SALES"
        MARKETING = "MARKETING", "MARKETING"
        OPERATIONS = "OPERATIONS", "OPERATIONS"

    department_id = models.AutoField(primary_key=True)
    parent_dept = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="parent_dept_id",
        related_name="sub_departments"
    )
    dept_code = models.CharField(
        max_length=20, null=True, blank=True
    )
    dept_name = models.CharField(max_length=100)
    dept_short_name = models.CharField(max_length=50)
    dept_type = models.CharField(
        max_length=10,
        choices=DepartmentType.choices,
        default=DepartmentType.OPERATIONS
    )
    allow_assignment = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.dept_name

    class Meta:
        db_table = "department"


class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    country = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
        db_column="country_id",
        related_name="branches"
    )
    branch_code = models.CharField(
        max_length=10, null=True, blank=True
    )
    branch_name = models.CharField(max_length=100)
    region = models.CharField(
        max_length=100, null=True, blank=True
    )
    city = models.CharField(
        max_length=100, null=True, blank=True
    )
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(
        max_length=20, null=True, blank=True
    )
    email = models.EmailField(
        max_length=100, null=True, blank=True
    )
    postal_code = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(
        max_length=100, null=True, blank=True
    )
    updated_by = models.CharField(
        max_length=100, null=True, blank=True
    )

    def __str__(self):
        return self.branch_name

    class Meta:
        db_table = "branch"


class Custodian(models.Model):

    class CustodianType(models.TextChoices):
        SUPPLIER = "SUPPLIER", "SUPPLIER"
        EMPLOYEE = "EMPLOYEE", "EMPLOYEE"
        EXTERNAL = "EXTERNAL", "EXTERNAL"

    custodian_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(
        Branch,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="branch_id",
        related_name="custodians"
    )
    dept = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="dept_id",
        related_name="custodians"
    )
    custodian_code = models.CharField(
        max_length=10, null=True, blank=True
    )
    custodian_name = models.CharField(max_length=100)
    custodian_type = models.CharField(
        max_length=10,
        choices=CustodianType.choices,
        default=CustodianType.SUPPLIER
    )
    phone = models.CharField(
        max_length=20, null=True, blank=True
    )
    email = models.EmailField(
        max_length=100, null=True, blank=True
    )
    can_hold_assets = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.custodian_name

    class Meta:
        db_table = "custodian"

# Create your models here.
