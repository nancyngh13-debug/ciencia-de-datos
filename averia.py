import matplotlib.pyplot as plt

# Datos de la simulación
meses = ['Mayo', 'Junio', 'Julio']
horas_paro = [1263, 520, 145]
promedio = [468, 494, 378]
linea_base = [80, 80, 80]

# Configuración de la figura
plt.figure(figsize=(10, 6))

# Trazar las líneas
plt.plot(meses, horas_paro, marker='o', color='#4472C4', linewidth=3, markersize=8, label='Horas de paro')
plt.plot(meses, promedio, marker='s', color='#ED7D31', linewidth=3, markersize=8, label='Promedio')
plt.plot(meses, linea_base, marker='o', color='#A5A5A5', linewidth=3, markersize=8)

# Añadir etiquetas de datos
for i, valor in enumerate(horas_paro):
    plt.text(i, valor + 30, f'{valor}', ha='center', va='bottom', fontsize=10)

for i, valor in enumerate(promedio):
    plt.text(i, valor + 30, f'{valor}', ha='center', va='bottom', fontsize=10, color='#ED7D31')

# Configuración de ejes y título
plt.title('HORAS DE PARO 2026', fontsize=16, fontweight='bold', pad=20)
plt.ylabel('Tiempo [h]', fontsize=14, fontweight='bold')
plt.ylim(0, 1400)
plt.grid(True, linestyle='-', alpha=0.3)

# Configuración de la leyenda
plt.legend(loc='upper left', bbox_to_anchor=(0, 1.15), frameon=False, ncol=2, fontsize=12)

# Quitar bordes superior y derecho para mayor limpieza
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Mostrar la gráfica
plt.tight_layout()
plt.show()