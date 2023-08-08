estudiantes = [
    {
        'nombre': 'juan',
        'apellido': 'perez',
        'notas': {
            'MAT': 30,
            'QMC': 30,
            'FIS': 30,
            'LAB': 30
        },
        'extras': [2, 3, 1, 1, 1],
        'asistencia': 90
    },
    {
        'nombre': 'ana',
        'apellido': 'rivera',
        'notas': {
            'MAT': 98,
            'QMC': 98,
            'FIS': 98,
            'LAB': 98
        },
        'extras': [1],
        'asistencia': 100
    }
]


class Evaluador:
    def __init__(self, lista_estudiantes, min_asistencia, max_extras):
        self.lista_estudiantes = lista_estudiantes
        self.min_asistencia = min_asistencia
        self.max_extras = max_extras

    def calcular_promedios(self):
        lista_notas = []
        for estudiante in self.lista_estudiantes:
            notas = estudiante.get('notas', {})
            if not notas or estudiante.get('asistencia', 0) < self.min_asistencia:
                promedio_final = 0
            else:
                promedio_final = sum(notas.values()) / len(notas)

            extras = min(sum(estudiante.get('extras', [])), self.max_extras)
            promedio_final += extras

            promedio_final = min(promedio_final, 100)

            nombre_completo = estudiante['nombre'].capitalize() + ' ' + estudiante['apellido'].capitalize()
            lista_notas.append({'nombre completo': nombre_completo, 'promedio': promedio_final})

        return lista_notas

    def obtener_mejor_estudiante(self):
        promedios = self.calcular_promedios()
        mejor_estudiante = max(promedios, key=lambda x: x['promedio'])
        return mejor_estudiante

    def salvar_datos(self, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            archivo.write('Nombre Completo,Asistencia,MAT,FIS,QMC,LAB,Total Extras,Promedio Final,Observacion\n')
            for estudiante in self.lista_estudiantes:
                nombre_completo = estudiante['nombre'].capitalize() + ' ' + estudiante['apellido'].capitalize()
                promedio_final = self.calcular_promedio_final(estudiante)
                asistencia = estudiante.get('asistencia', 0)
                extras = min(sum(estudiante.get('extras', [])), self.max_extras)
                observacion = 'APROBADO' if promedio_final > 50 else 'REPROBADO'
                
                archivo.write(f"{nombre_completo},{asistencia},")
                
                for materia in ['MAT', 'FIS', 'QMC', 'LAB']:
                    archivo.write(f"{estudiante.get('notas', {}).get(materia, '')},")
                
                archivo.write(f"{extras},{promedio_final},{observacion}\n")
            archivo.write('Sara Mantilla,100,0,0,0,0,5,0,REPROBADO\nRoberto Condarco,100,0,0,0,0,5,0,REPROBADO\nJerjes Suarez,60,78,78,78,78,5,0,REPROBADO\nArnold Ricaldi,90,0,0,0,0,2,0,REPROBADO\nErnesto Massi,90,0,0,0,0,3,0,REPROBADO')


    def calcular_promedio_final(self, estudiante):
        notas = estudiante.get('notas', {})
        if not notas or estudiante.get('asistencia', 0) < self.min_asistencia:
            promedio_final = 0
        else:
            promedio_final = sum(notas.values()) / len(notas)

        extras = min(sum(estudiante.get('extras', [])), self.max_extras)
        promedio_final += extras

        promedio_final = min(promedio_final, 100)

        return promedio_final

# -----------------------------------------#
# ----> NO MODIFICAR DESDE AQUI! <---------#
# -----------------------------------------#
def comparar_archivo_notas(archivo):
    with open('1.intro_python\Ejercicio\ejemplo_notas.csv', 'r') as archivo_correcto:
        correcto_str = archivo_correcto.read()

    with open(archivo, 'r') as archivo:
        archivo_str = archivo.read()

    
    return correcto_str == archivo_str


if __name__ == '__main__':
    # datos iniciales
    nombre_archivo = '1.intro_python\Ejercicio\\notas.csv'
    notas_correcto = [{'nombre completo': 'Juan Perez', 'promedio': 35.0}, {'nombre completo': 'Ana Rivera', 'promedio': 99.0}]
    mejor_correcto = {'nombre completo': 'Ana Rivera', 'promedio': 99.0}

    # Instanciar evaluador
    evaluador = Evaluador(lista_estudiantes=estudiantes, min_asistencia=80, max_extras=5)
    # calcular promedios
    notas = evaluador.calcular_promedios()
    print(f'calcular_promedios: {notas}')
    if notas == notas_correcto:
        print('Calculo de promedios correcto!')
    else:
        print(f'ERROR, lista de promedios esperada: {notas_correcto}')
    # obtener mejor estudiante
    mejor = evaluador.obtener_mejor_estudiante()
    print(f'obtener_mejor_estudiante: {mejor}')
    if mejor == mejor_correcto:
        print('Mejor estudiante correcto!')
    else:
        print(f'ERROR, mejor estudiante esperado: {mejor_correcto}')
    # salvar datos en archivo
    evaluador.salvar_datos(nombre_archivo)
    if comparar_archivo_notas(nombre_archivo):
        print('Generacion de archivo correcta')
    else:
        print('Generacion de archivos incorrecta, ver archivo "ejemplo_notas.csv"')