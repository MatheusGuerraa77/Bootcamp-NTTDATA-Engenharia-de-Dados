from datetime import datetime, timezone, timedelta

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sao_Paulo = datetime.now(timezone(timedelta(hours=-3)))

print(data_oslo)
print(data_sao_Paulo)