from django.core.management.base import BaseCommand
from dispositivos.models import Category, Product, AlertRule, ProductAlertRule

class Command(BaseCommand):
	help = "Carga catálogo en español (categorías, productos, alertas y overrides)"

	def handle(self):
		cat_il, _ = Category.objects.get_or_create(name="Iluminación")
		Category.objects.get_or_create(name="Climatización")
		Category.objects.get_or_create(name="Computación")

		p1, _ = Product.objects.get_or_create(
			sku="LED-50W",
			defaults=dict(
				name="Panel LED 50W",
				category=cat_il,
				manufacturer="ECOLUZ",
				model_name="PL-50",
				description="Panel LED para oficinas con alta eficiencia.",
				nominal_voltage=220,
				max_current=0.25,
				standby_power=1.0
			)
		)
		# ... crea p2, p5 similar ...

		r1, _ = AlertRule.objects.get_or_create(
			name="Consumo alto",
			severity="HIGH",
			defaults=dict(unit="kWh", default_max_threshold=50.0)
		)
		AlertRule.objects.get_or_create(
			name="Consumo en espera elevado",
			severity="MEDIUM",
			defaults=dict(unit="kWh", default_max_threshold=0.3)
		)
		AlertRule.objects.get_or_create(
			name="Bajo rendimiento",
			severity="LOW",
			defaults=dict(unit="kWh", default_min_threshold=0.5)
		)

		ProductAlertRule.objects.get_or_create(product=p1, alert_rule=r1, defaults=dict(max_threshold=2.0))
		# ... el resto de overrides ...

		self.stdout.write(self.style.SUCCESS('Catálogo cargado correctamente'))