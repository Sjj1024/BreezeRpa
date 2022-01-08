from petal import ETL
import pandas as pd


def lnglat2wkt(s: str) -> str:
  """输出结果可以使用petal中的norm_wkt_geometry转成地理格式以及转坐标"""
  if s and not pd.isna(s):
    s = s.rstrip(';') + ';'
    if len(s.split(';')) <= 3:
      return None
    else:
      lnglat = (s + s.split(';')[0]).replace(',', ' ').replace(';', ', ')
    return f'MULTIPOLYGON ((({lnglat})))'
  else:
    return None


df_res = (
  ETL()
  .from_dict({'geometry': ['110.158801,20.01362;110.171449,19.997316;110.174323,20.05546;110.195595,20.053422;110.185965,20.028836;110.198901,20.042963;110.171521,20.052268;110.173676,20.026119;110.169077,20.040926;110.161459,20.041197;110.190493,20.046223;110.17497,20.047174;110.174826,20.039567;110.160453,20.040247;110.161028,20.040247;110.161747,20.067819;110.162322,20.043099;110.15801,20.02313;110.157579,20.021636;110.157579,20.022451']})
  .apply_column(lnglat2wkt, src_col='geometry')
  .norm_wkt_geometry()
  .returns()
)
print(df_res)
