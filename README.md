## Описание датасета

Датасет аггрегирует информацию о заказах в Бразилии и исторические метеоданные в день заказа по координатам

## Задача датасета

Найти зависимость между заказами покупателей и погодой на улице в день заказа.

## Гипотезы

Данный датасет позволяет проверить следующие гипотезы

- Есть зависимость между частотой заказов и погодой на улице
- Покупки товаров в определенных категориях зависят от погоды

## Использование

``` 
 import pandas as pd
 
 df = pd.read_csv('data/orders.csv')
 ```

## Структура датасета

```
df.info()
```

### Колонки
```shell
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 107802 entries, 0 to 107801
Data columns (total 36 columns):
 #   Column                         Non-Null Count   Dtype  
---  ------                         --------------   -----  
 0   timestamp                      107802 non-null  object 
 1   payment_value                  107802 non-null  float64
 2   zip_code                       107802 non-null  float64
 3   city                           107802 non-null  object 
 4   state                          107802 non-null  object 
 5   latitude                       107802 non-null  float64
 6   longitude                      107802 non-null  float64
 7   items_quant                    107802 non-null  float64
 8   product_category               107802 non-null  object 
 9   date                           107802 non-null  object 
 10  time                           107802 non-null  object 
 11  weekday                        107802 non-null  object 
 12  apparent_temperature_max       107802 non-null  float64
 13  apparent_temperature_min       107802 non-null  float64
 14  et0_fao_evapotranspiration     107802 non-null  float64
 15  precipitation_hours            107802 non-null  float64
 16  precipitation_sum              107802 non-null  float64
 17  rain_sum                       107802 non-null  float64
 18  snowfall_sum                   107802 non-null  float64
 19  sunrise                        107802 non-null  object 
 20  sunset                         107802 non-null  object 
 21  weathercode                    107802 non-null  float64
 22  winddirection_10m_dominant     106933 non-null  float64
 23  windgusts_10m_max              107802 non-null  float64
 24  windspeed_10m_max              107802 non-null  float64
 25  cloud_cover_total_mean_%       107802 non-null  float64
 26  cloudcover_high_mean_%         107802 non-null  float64
 27  cloudcover_low_mean_%          107802 non-null  float64
 28  cloudcover_mid_mean_%          107802 non-null  float64
 29  surface_pressure_mean_hPa      107802 non-null  float64
 30  temperature_2m_max             107802 non-null  float64
 31  temperature_2m_min             107802 non-null  float64
 32  temperature_2m_hourly          107802 non-null  float64
 33  precipitation_hourly           107802 non-null  float64
 34  relative_humidity_2m_hourly    107802 non-null  float64
 35  daily_shortwave_radiation_sum  107802 non-null  float64
dtypes: float64(27), object(9)
memory usage: 29.6+ MB
```

```shell
- timestamp                         временная метка заказа в локальной таймзоне
- payment_value                     сумма транзакции
- zip_code                          индекс покупателя
- city                              город покупателя
- state                             штат
- latitude                          широта
- longitude                         долгота
- items_quant                       количество товаров в заказе
- product_category                  категория продукта (англ)
- date                              дата заказа
- time                              время заказа
- weekday                           день заказа
- apparent_temperature_max          суточная максимальная температура (по ощущениям)
- apparent_temperature_min          суточная минимальная температура (по ощущениям)
- et0_fao_evapotranspiration        суточная эвапотранспирация (количество испаряемой влаги) 
- precipitation_hours               суточное количество часов, когда шёл дождь          
- precipitation_sum                 суточное количество осадков, включая дождь, снег (мм)
- rain_sum                          суточная количество осадков (дождь) (мм)
- snowfall_sum                      суточное количество осадков (снег) (мм)          
- sunrise                           время рассвета (iso8601)
- sunset                            время заката (iso8601)
- weathercode                       код погоды (WMO code)
- winddirection_10m_dominant        доминирующее направление ветра (°)
- windgusts_10m_max                 максимальная порывы ветра за сутки (km/h)
- windspeed_10m_max                 максимальная скорость ветра за сутки (km/h)
- cloud_cover_total_mean_%          процент общей облачности (%) 
- cloudcover_high_mean_%            облака на высоте от 6 километров (%)
- cloudcover_low_mean_%             облака и туман на высоте до 2х километров (%)
- cloudcover_mid_mean_%             облака на высоте от 2х до 6 километров (%)   
- surface_pressure_mean_hPa         атмосферное давление за день (hPa)
- temperature_2m_max                максимальная дневная температура, два метра над землей (C°)
- temperature_2m_min                минимальная дневная температура, два метра над землей (C°)
- daily_shortwave_radiation_sum     суммарная солнечная радиация за день в МегаДжоулях (MJ/m²)
- temperature_2m_hourly             температура на момент заказа (C°)
- precipitation_hourly              количество осадков за предыдущий час (дождь, снег)
- relative_humidity_2m_hourly       относительная влажность, 2 метра над землей (%)
```

### Описание полей



## Источники данных

***Meteo-Api:*** https://open-meteo.com/en/docs/historical-weather-api \

```shell
curl https://archive-api.open-meteo.com/v1/era5?latitude=-23.55&longitude=-46.64&start_date=2022-11-19&end_date=2022-11-19&hourly=temperature_2m,relativehumidity_2m,precipitation&daily=weathercode,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset,shortwave_radiation_sum,precipitation_sum,rain_sum,snowfall_sum,precipitation_hours,windspeed_10m_max,windgusts_10m_max,winddirection_10m_dominant,et0_fao_evapotranspiration&timezone=America%2FSao_Paulo
```

```json
{
  "latitude": -23.75,
  "longitude": -47.0,
  "generationtime_ms": 0.6819963455200195,
  "utc_offset_seconds": -10800,
  "timezone": "America/Sao_Paulo",
  "timezone_abbreviation": "-03",
  "elevation": 939.0,
  "hourly_units": {
    "time": "iso8601",
    "temperature_2m": "°C",
    "relativehumidity_2m": "%",
    "precipitation": "mm"
  },
  "hourly": {
    "time": [
      "2022-11-19T00:00",
      "2022-11-19T01:00",
      "2022-11-19T02:00",
      "2022-11-19T03:00",
      "2022-11-19T04:00",
      "2022-11-19T05:00",
      "2022-11-19T06:00",
      "2022-11-19T07:00",
      "2022-11-19T08:00",
      "2022-11-19T09:00",
      "2022-11-19T10:00",
      "2022-11-19T11:00",
      "2022-11-19T12:00",
      "2022-11-19T13:00",
      "2022-11-19T14:00",
      "2022-11-19T15:00",
      "2022-11-19T16:00",
      "2022-11-19T17:00",
      "2022-11-19T18:00",
      "2022-11-19T19:00",
      "2022-11-19T20:00",
      "2022-11-19T21:00",
      "2022-11-19T22:00",
      "2022-11-19T23:00"
    ],
    "temperature_2m": [
      13.0,
      13.0,
      12.6,
      12.6,
      12.7,
      12.3,
      12.8,
      15.5,
      16.9,
      18.0,
      19.0,
      20.6,
      22.0,
      22.4,
      21.9,
      21.1,
      19.7,
      17.8,
      16.8,
      15.7,
      15.7,
      15.5,
      15.5,
      15.4
    ],
    "relativehumidity_2m": [
      93,
      93,
      94,
      94,
      93,
      94,
      92,
      83,
      76,
      71,
      68,
      65,
      61,
      60,
      66,
      71,
      78,
      84,
      86,
      91,
      90,
      91,
      91,
      91
    ],
    "precipitation": [
      0.00,
      0.00,
      0.00,
      0.00,
      0.00,
      0.00,
      0.00,
      0.00,
      0.00,
      0.00,
      0.00,
      0.00,
      0.00,
      0.00,
      0.00,
      0.00,
      0.00,
      0.00,
      0.00,
      0.00,
      0.00,
      0.00,
      0.00,
      0.00
    ]
  },
  "daily_units": {
    "time": "iso8601",
    "weathercode": "wmo code",
    "temperature_2m_max": "°C",
    "temperature_2m_min": "°C",
    "apparent_temperature_max": "°C",
    "apparent_temperature_min": "°C",
    "sunrise": "iso8601",
    "sunset": "iso8601",
    "shortwave_radiation_sum": "MJ/m²",
    "precipitation_sum": "mm",
    "rain_sum": "mm",
    "snowfall_sum": "cm",
    "precipitation_hours": "h",
    "windspeed_10m_max": "km/h",
    "windgusts_10m_max": "km/h",
    "winddirection_10m_dominant": "°",
    "et0_fao_evapotranspiration": "mm"
  },
  "daily": {
    "time": [
      "2022-11-19"
    ],
    "weathercode": [
      3
    ],
    "temperature_2m_max": [
      22.4
    ],
    "temperature_2m_min": [
      12.3
    ],
    "apparent_temperature_max": [
      24.8
    ],
    "apparent_temperature_min": [
      11.2
    ],
    "sunrise": [
      "2022-11-19T05:11"
    ],
    "sunset": [
      "2022-11-19T18:32"
    ],
    "shortwave_radiation_sum": [
      26.39
    ],
    "precipitation_sum": [
      0.00
    ],
    "rain_sum": [
      0.00
    ],
    "snowfall_sum": [
      0.00
    ],
    "precipitation_hours": [
      0.0
    ],
    "windspeed_10m_max": [
      20.6
    ],
    "windgusts_10m_max": [
      44.3
    ],
    "winddirection_10m_dominant": [
      326
    ],
    "et0_fao_evapotranspiration": [
      4.38
    ]
  }
}
```


***Source Orders Data:*** https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce


## Создатели датасета




