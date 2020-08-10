# BikeBot
Notify when bikes that can be resold for profit are posted on Kijiji

## Install
### Manually
```bash
git clone https://github.com/Jonathancui123/BikeBot.git
cd BikeBot
pip install -r requirements.txt
```
Next, install the kijiji scraper that BikeBot depends on. Credit to https://github.com/CRutkowski for the scraper

```bash
git clone https://github.com/CRutkowski/Kijiji-Scraper.git
cd Kijiji-Scraper
python3 setup.py install
cd ..
```
Kijiji-Scraper should be a subfolder within the project. Next, copy the custom config file for the scraper.

```bash
copy config.yaml .\\Kijiji-Scraper\\config.yaml
```