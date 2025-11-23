# NASA 3I/ATLAS Image Manifest

Этот документ связывает официальные изображения 3I/ATLAS (с сайтов NASA/ESA)
с локальными файлами в репозитории и краткими комментариями.

## Table structure

Для каждого изображения фиксируются:

- `id` — короткий идентификатор внутри лаборатории;
- `date_obs` — дата наблюдения (UTC, по возможности);
- `mission_instrument` — миссия и инструмент (SOHO LASCO, MAVEN, Perseverance Mastcam-Z и т.п.);
- `source_url` — ссылка на оригинальную страницу NASA/ESA;
- `local_filename` — имя файла в `data/raw/nasa/` (если уже скачано);
- `channel` — диапазон (optical / UV / combined / other);
- `notes_ru` / `notes_en` — краткие комментарии.

## Image entries (initial draft)

| id                | date_obs     | mission_instrument        | source_url | local_filename                    | channel  | notes_ru | notes_en |
|-------------------|-------------:|---------------------------|-----------|-----------------------------------|----------|----------|----------|
| `SOHO_C3_2025-10` | 2025-10-15–26 | SOHO / LASCO C3 coronagraph | *TBD*    | `data/raw/nasa/soho_c3_oct15-26.png` | optical | Слабое желтоватое пятно на зернистом фоне; 3I/ATLAS едва ярче шума, видна только при внимательном рассмотрении. | Faint, slightly yellowish point against a grainy background; 3I/ATLAS is only marginally brighter than the noise. |
| `MAVEN_UV_2025-10-09` | 2025-10-09 | MAVEN / UV instrument     | *TBD*    | `data/raw/nasa/maven_uv_2025-10-09.png` | UV       | Кома газа и пыли вокруг ядра; структура больше похожа на ореол, чем на «классический хвост». | Gas-and-dust coma around the nucleus; more like a diffuse halo than a classical narrow tail. |
| `PERSEVERANCE_MASTCAMZ_2025-10-04` | 2025-10-04 | Perseverance / Mastcam-Z | *TBD* | `data/raw/nasa/perseverance_mastcamz_2025-10-04.png` | optical | 3I/ATLAS как слабое смазанное пятно среди звёздного поля, снято с поверхности Марса. | 3I/ATLAS as a faint smudge among background stars, imaged from the surface of Mars. |

> **Примечание.** Поля `source_url` пока отмечены как `*TBD*`.  
> Их можно позже заполнить прямыми ссылками из:
> - NASA 3I/ATLAS image gallery,  
> - официальных новостных страниц с описанием изображений.


