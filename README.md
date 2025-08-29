# 📊 Web Scraping del S&P 500 con Selenium y Matplotlib

Este proyecto realiza web scraping de datos históricos del índice S&P 500 desde Yahoo Finance y genera visualizaciones interactivas utilizando Python, Selenium y Matplotlib.

## 🚀 Características

- Extracción automática de datos en tiempo real del S&P 500
- Visualización de precios de cierre históricos (6 meses)
- Gráfica de variación porcentual diaria
- Estadísticas detalladas del rendimiento del índice
- Ejecución en modo headless (sin interfaz gráfica)

## 📦 Requisitos Previos

### Software necesario:
- Python 3.8+
- Google Chrome
- ChromeDriver (compatible con tu versión de Chrome)

### Instalación de dependencias:
```bash
pip install selenium pandas matplotlib
```

### Configuración de ChromeDriver:
1. Descarga ChromeDriver desde: https://sites.google.com/chromium.org/driver/
2. Asegúrate de que la versión coincida con tu navegador Chrome
3. Agrega ChromeDriver al PATH del sistema o colócalo en el directorio del proyecto

## 🛠️ Estructura del Proyecto

```
scraping-S&P-500/
├── output_data/
|   └── result.png       # Resultado de las graficas
├── src/
│   └── main.py          # Script principal de scraping y visualización
├── requirements.txt     # Dependencias del proyecto
├── README.md           # Este archivo
```

## 📋 Funcionalidades

### Extracción de Datos:
- Precio actual del S&P 500
- Cambio diario en puntos y porcentaje
- Datos históricos de 6 meses
- Precios de cierre diarios

### Visualizaciones:
1. **Gráfica de Línea**: Tendencia de precios de cierre
2. **Gráfica de Barras**: Variación porcentual diaria (coloreada)
   - Verde: días positivos
   - Rojo: días negativos

### Estadísticas:
- Precio máximo y mínimo del período
- Volatilidad promedio
- Precio actual y cambio del día

## 🎯 Uso

### Ejecución básica:
```bash
python src/main.py
```

### Ejecución con opciones:
```bash
# Ejecutar en modo visible (sin headless)
# Modifica el script: remove "--headless" de chrome_options
python src/main.py
```

### Salida esperada:
- Gráficas interactivas de matplotlib
- Estadísticas en consola
- Datos procesados en formato DataFrame

## ⚠️ Consideraciones Legales

Este proyecto es para fines educativos y de demostración. Asegúrate de:

1. ✅ Respetar `robots.txt` de Yahoo Finance
2. ✅ No realizar requests excesivas
3. ✅ Cumplir con los términos de servicio
4. ✅ Usar headers apropiados y rate limiting
5. ✅ Considerar el uso de APIs oficiales para producción

## 🔧 Solución de Problemas

### Error común: "ChromeDriver not found"
- Verifica que ChromeDriver esté en el PATH
- Asegúrate de que las versiones de Chrome y ChromeDriver coincidan

### Error: "Element not found"
- Yahoo Finance puede cambiar su estructura HTML
- Revisa los selectores CSS en el código
- Usa el screenshot de debug para diagnóstico

## 📊 Ejemplo de Salida

```
Precio actual del S&P 500: 4,567.25
Cambio: +25.50 (+0.56%)
Precio más alto (6 meses): $4,589.12
Precio más bajo (6 meses): $4,102.45
Volatilidad promedio: 0.85%
```

Resultados de las graficas se guardan en esta carpeta
```
├── output_data/
    └── result.png       # Resultado de las graficas
```

## 🎨 Personalización

### Modificar el período de tiempo:
Cambia el selector en el código:
```python
# De:
time_period_button = driver.find_element(By.CSS_SELECTOR, "button[value='6_M']")
# A:
time_period_button = driver.find_element(By.CSS_SELECTOR, "button[value='1_M']")  # 1 mes
# o "button[value='1_Y']]" para 1 año
```

### Personalizar gráficas:
Modifica los parámetros de matplotlib en las secciones:
- `ax1.plot()` - Gráfica principal
- `ax2.bar()` - Gráfica de variación

## 📝 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Haz fork del proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📞 Soporte

Si encuentras problemas:
1. Revisa los mensajes de error en consola
2. Verifica que todas las dependencias estén instaladas
3- Asegúrate de que ChromeDriver esté correctamente configurado

---

**Nota**: Este proyecto requiere una conexión a internet activa para funcionar correctamente.
