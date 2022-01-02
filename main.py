import builtins
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

st.dataframe(df.style.highlight_max(axis=0),200,100)

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""
st.write('df2ここから')
df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

st.write('df3ここから')
df3 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [34.8370,134.6897],
    columns=['lat','lon']
)
st.map(df3)

# st.write('Display Image')

# 10. インタラクティブなウィジェット , 11. レイアウトを整える
left_column,right_column = st.columns(2)

left_column.header("Display Image")
if left_column.checkbox('Show Image'):
    img = Image.open('./Himeji_Castle.jpg')
    left_column.image(img, caption='Himeji Castle',use_column_width=True)

right_column.header("Select Box")
option = right_column.selectbox(
    'Select a number',
    list(range(1,10))
)
option_str = f'{option} '+ ' is selected'
right_column.write(option_str)

button = right_column.button('Show Message on right column.')
if button:
    right_column.write('Orz')

st.sidebar.write('Interactive widgets')
text = st.sidebar.text_input('Enter your hobby.')
st.sidebar.write('Your hobby is', text)

condition = st.sidebar.slider('How are you?')
st.sidebar.write('Your condition:',condition)

expander = st.expander('問い合わせ')
expander.write('問い合わせの回答')

#12. プレグレスバーの表示
st.write('プレグレスバーの表示')
'Start'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!!'