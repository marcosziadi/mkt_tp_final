# 🧩 EcoBottle Data Warehouse & ETL Ecosystem

---

## 📘 Descripción del Proyecto

EcoBottle AR es una empresa argentina que comercializa **botellas reutilizables** a través de canales online y tiendas físicas en distintas provincias del país.

El objetivo de este proyecto fue diseñar e implementar un mini–ecosistema de datos comercial (**online + offline**) que permita consolidar información de ventas, clientes, envíos, pagos y actividad digital, generando un **Data Warehouse con estructura de modelo estrella**.

El producto final incluye:

* Scripts **ETL en Python** (`pandas`) para extraer, transformar y cargar los datos desde archivos RAW.
* Un modelo **Data Warehouse** con tablas de hechos y dimensiones.
* Un **Dashboard en Power BI** con KPIs clave:
    * Ventas totales
    * Usuarios activos
    * Ticket promedio
    * NPS
    * Ventas por provincia
    * Ranking mensual por producto

---

## 🏗️ Estructura del Repositorio

```bash
├── data/
│   ├── raw/                # Datos originales (.csv)
│   ├── staging/            # Datos limpios y transformados
│   └── warehouse/          # Tablas finales del Data Warehouse
│
├── docs/
│   └── assets/             # Diagramas e imágenes
│
├── src/
│   └── etl/
│       ├── extract/        # Extracción de datos desde raw/
│       ├── transform/      # Limpieza, modelado y creación de dimensiones / hechos
│       ├── load/           # Carga en staging y warehouse
│       └── pipeline.py     # Orquestador del proceso ETL completo
│
├── dashboard/              # Archivos del dashboard
├── requirements.txt        # Dependencias del entorno virtual
├── LICENSE                 # Licencia MIT
└── README.md               # Este archivo
```

---

## ⚙️ Instrucciones de Ejecución

Para reproducir el ambiente y el proceso ETL, sigue los siguientes pasos:

### 1️⃣ Clonar el repositorio

```bash
git clone [https://github.com/](https://github.com/)<tu-usuario>/EcoBottle-Data-Warehouse-ETL.git
cd EcoBottle-Data-Warehouse-ETL
```

### 2️⃣ Crear entorno virtual e instalar dependencias

```bash
python -m venv venv
# En macOS/Linux
source venv/bin/activate
# En Windows
venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Ejecutar el pipeline ETL completo

```bash
python src/etl/pipeline.py
```

Este script ejecuta en orden las etapas de:

* Extract: lectura de archivos RAW
* Transform: limpieza, normalización y creación de dimensiones/hechos
* Load: exportación final a /data/warehouse/

---

## 📊 Dashboard en Power BI

El tablero integra todas las tablas del Data Warehouse y permite explorar los principales indicadores de negocio mediante filtros de fecha, canal, provincia y producto.

### 📍 Captura del dashboard final:

---

## 🧱 Modelado de Datos
El modelo de datos sigue la metodología Kimball (modelo estrella), utilizando prefijos dim_ y fact_ para distinguir dimensiones y hechos.

### 📘 Diagrama Entidad–Relación (modelo fuente):
Tablas Principales del Data Warehouse

### Tablas Principales del Data Warehouse

| Tipo | Tabla | Descripción |
| :--- | :--- | :--- |
| **Dimensión** | `dim_customer` | Información de clientes. |
| **Dimensión** | `dim_channel` | Canales de venta. |
| **Dimensión** | `dim_store` | Tiendas físicas, con dirección y provincia. |
| **Dimensión** | `dim_address` | Direcciones normalizadas. |
| **Dimensión** | `dim_product` | Productos. |
| **Dimensión** | `dim_calendar` | Dimensión temporal. |
| **Hecho** | `fact_sales_order` | Cada fila representa una orden de venta. |
| **Hecho** | `fact_sales_order_item` | Cada fila representa un ítem dentro de una orden de venta. |
| **Hecho** | `fact_payment` | Cada fila representa un pagos asociado a una orden. |
| **Hecho** | `fact_shipment` | Cada fila representa un envio de una orden. |
| **Hecho** | `fact_web_session` | Cada fila representa una sesión web. |
| **Hecho** | `fact_nps_response` | Cada fila representa una respuesta de encuesta NPS. |

---

## 🧩 Supuestos y Decisiones de Diseño

* Las claves foráneas nulas se reemplazaron por el valor -1 para mantener la integridad referencial.
* Las fechas fueron integradas a una única dimensión dim_calendar utilizada por todas las tablas de hechos.

---

## 📜 Licencia

Este proyecto se distribuye bajo la **Licencia MIT**, lo que permite su uso, modificación y distribución con fines académicos o profesionales, manteniendo los créditos originales.

[Ver archivo LICENSE para más información.](LICENSE)

---

## 👨‍💻 Autor

**Marcos Ziadi**

📍 Rosario, Santa Fe, Argentina

📧 139mziadi@gmail.com

🔗 [LinkedIn](<[Tu-Link-De-LinkedIn](https://www.linkedin.com/in/marcos-ziadi/)>) | [GitHub](<[Tu-Link-De-GitHub](https://github.com/marcosziadi/)>)
