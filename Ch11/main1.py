import pandas as pd
import os

df = pd.DataFrame([["김메가", "1980.01.02", "2026-0001"],
                   ["박서울", "1985.02.04", "2026-0002"],
                   ["김진흥", "1990.06.12", "2026-0003"],
                   ["최선린", "1995.10.23", "2026-0004"],
                   ["이고려", "2000.05.03", "2026-0005"],
                   ["성연세", "2005.12.31", "2026-0006"]])

print(df)
file_path = os.path.join(os.path.dirname(__file__), '수료증명단.xlsx')
df.to_excel(file_path, index=False, header=False)