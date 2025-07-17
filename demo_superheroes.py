"""
S.O.L.I.D principles: a practical approach.

Lady Berrocal
Óscar Rodríguez
"""

from rich.console import Console
from abc import ABC, abstractmethod  # 👈 Importamos para clases abstractas

console = Console()

# 🟡 S - RESPONSABILIDAD ÚNICA
console.print("[bold blue]S - Responsabilidad Única[/bold blue]")
console.print("[bold blue]Cada clase debe tener una única responsabilidad clara.[/bold blue]")
console.print("[bold blue]Por ejemplo, la clase SuperHeroe solo se encarga de almacenar información del héroe y presentarlo.[/bold blue]")
console.print("[bold blue]No tiene otras funciones como COMBATIR o REPORTAR.[/bold blue]")
console.print("-" * 60)

class SuperHeroe:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder

    def presentarse(self):
        print(f"🦸 Hola, soy {self.nombre} y mi poder es {self.poder}")

# 🟠 O - ABIERTO/CERRADO
console.print("[bold magenta]O - Abierto/Cerrado[/bold magenta]")
console.print("[magenta]El código debe estar abierto para EXTENDERLO, pero cerrado para MODIFICARLO.[/magenta]")
console.print("[magenta]Aquí la clase Mision es ahora abstracta, y nuevas misiones la heredan sin tocarla.[/magenta]")
console.print("-" * 60)

class Mision(ABC):  # 👈 Ahora es una clase abstracta
    @abstractmethod
    def ejecutar(self):
        pass

class DesastreNatural(Mision):
    def ejecutar(self):
        print("🌪️ Emergencia: terremoto y tormenta en la ciudad")

class InvasionOvni(Mision):
    def ejecutar(self):
        print("🛸 Alerta: invasión OVNI detectada en el cielo")

# 🔵 L - SUSTITUCIÓN DE LISKOV
console.print("[bold cyan]L - Sustitución de Liskov[/bold cyan]")
console.print("[cyan]Todas las subclases deben funcionar como su clase padre sin causar errores.[/cyan]")
console.print("-" * 60)

def iniciar_mision(mision: Mision):
    mision.ejecutar()

# 🟢 I - SEGREGACIÓN DE INTERFACES
console.print("[bold yellow]I - Segregación de Interfaces[/bold yellow]")
console.print("[yellow]Los héroes implementan solo las interfaces que necesitan.[/yellow]")
console.print("-" * 60)

class PuedeVolar:
    def volar(self):
        pass

class PuedeUsarTecnologia:
    def usar_traje(self):
        pass

class PuedeGolpearFuerte:
    def golpear_fuerte(self):
        pass

class Superwoman(SuperHeroe, PuedeVolar):
    def volar(self):
        print(f"{self.nombre} vuela entre los edificios 🕊️")

class Ironman(SuperHeroe, PuedeUsarTecnologia):
    def usar_traje(self):
        print(f"{self.nombre} activa su traje de combate 🔥")

class Hulk(SuperHeroe, PuedeGolpearFuerte):
    def golpear_fuerte(self):
        print(f"{self.nombre} da un puñetazo enorme 💥")

class Batman(SuperHeroe):
    def usar_gadgets(self):
        print(f"{self.nombre} utiliza sus gadgets y visión nocturna 🦇")

# 🔴 D - INVERSIÓN DE DEPENDENCIAS
console.print("[bold red]D - Inversión de Dependencias[/bold red]")
console.print("[red]La lógica depende de abstracciones, no de clases concretas.[/red]")
console.print("-" * 60)

class Comunicador:
    def enviar_mensaje(self, mensaje):
        pass

class ComunicadorEmail(Comunicador):
    def enviar_mensaje(self, mensaje):
        print(f"[📧 Email] {mensaje}")

class ComunicadorApp(Comunicador):
    def enviar_mensaje(self, mensaje):
        print(f"[📱 App] {mensaje}")

class InformeMision:
    def __init__(self, comunicador: Comunicador):
        self.comunicador = comunicador

    def enviar_informe(self, heroe: SuperHeroe):
        mensaje = f"{heroe.nombre} ha completado su misión ✅"
        self.comunicador.enviar_mensaje(mensaje)

# 🏁 EJECUCIÓN DEL PROGRAMA
console.print("[bold green]🚀 INICIANDO MISIONES DE LOS SUPERHÉROES[/bold green]")
console.print("-" * 60)

if __name__ == "__main__":
    batman = Batman("Batman", "estrategia y gadgets")
    superwoman = Superwoman("Superwoman", "vuelo y fuerza")
    ironman = Ironman("Ironman", "traje tecnológico")
    hulk = Hulk("Hulk", "fuerza imparable")

    mision_1 = DesastreNatural()
    mision_2 = InvasionOvni()

    email = ComunicadorEmail()
    app = ComunicadorApp()

    informe_email = InformeMision(email)
    informe_app = InformeMision(app)

    batman.presentarse()
    mision_2.ejecutar()
    batman.usar_gadgets()
    informe_app.enviar_informe(batman)

    console.print("-" * 60)

    superwoman.presentarse()
    mision_1.ejecutar()
    superwoman.volar()
    informe_email.enviar_informe(superwoman)

    console.print("-" * 60)

    ironman.presentarse()
    mision_2.ejecutar()
    ironman.usar_traje()
    informe_email.enviar_informe(ironman)

    console.print("-" * 60)

    hulk.presentarse()
    mision_1.ejecutar()
    hulk.golpear_fuerte()
    informe_app.enviar_informe(hulk)

    console.print("[bold green]✅ Todas las misiones han sido completadas exitosamente.[/bold green]\n")
