# 🚁 Optimización de Trayectorias de Drones Aplicadas al Cálculo Vectorial

## 📌 Descripción

Este proyecto presenta el desarrollo de un prototipo computacional para la representación y análisis de trayectorias de drones en un entorno tridimensional.

El prototipo utiliza conceptos de cálculo vectorial para modelar el terreno, representar la trayectoria del dron y comparar una ruta optimizada con una ruta no optimizada, considerando obstáculos y variaciones de altitud dentro del entorno de simulación.

La visualización se realiza en un espacio tridimensional interactivo, permitiendo observar el comportamiento de las diferentes trayectorias.

---

## 🎯 Objetivo

Desarrollar un prototipo computacional que permita representar y analizar trayectorias de drones mediante conceptos de cálculo vectorial, con el propósito de visualizar y comparar diferentes rutas dentro de un entorno tridimensional.

---

## 📐 Conceptos matemáticos

El proyecto aborda los siguientes conceptos de cálculo vectorial:

- 🗻 **Campos escalares:** utilizados para representar el terreno y sus variaciones de altitud.
- 📍 **Funciones vectoriales:** utilizadas para representar la posición y trayectoria del dron.
- 💨 **Campos vectoriales:** considerados para representar la influencia de factores externos sobre el desplazamiento.
- 📈 **Gradiente:** relacionado con la dirección de mayor variación del costo.
- ⚙️ **Multiplicadores de Lagrange:** relacionados con la optimización bajo restricciones.
- ∫ **Integrales múltiples:** relacionadas con el cálculo acumulado de magnitudes dentro del entorno.

> **Nota:** El gradiente, los multiplicadores de Lagrange y las integrales múltiples forman parte del fundamento teórico de optimización del proyecto. Los campos escalares y las funciones vectoriales son los conceptos implementados directamente en el prototipo.

---

## 💻 Tecnologías utilizadas

- 🐍 **Python**
- 🔢 **NumPy:** utilizada para realizar cálculos numéricos y generar los datos del entorno.
- 📊 **Plotly:** utilizada para crear la visualización tridimensional interactiva.

---

## 📦 Instalación

Para ejecutar el proyecto es necesario tener **Python** instalado.

Posteriormente, se deben instalar las bibliotecas utilizadas:

```bash
pip install numpy plotly
