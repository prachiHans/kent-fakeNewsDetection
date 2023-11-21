import subprocess

def install(package, version=None):
  if version is None:
    subprocess.call(['pip', 'install', package])
  else:
    subprocess.call(['pip', 'install', f'{package}=={version}'])

# Install the required packages

install('jupyterlab')
install('jupyter')
install('voila')
install('numpy')
install('pandas')
install('wordcloud')
install('matplotlib')
install('sklearn')
install('nltk')
install('seaborn')
install('pydantic', '2.2.0')
install('pydantic_core', '2.6.0')
install('fastapi')
install('Flash')
install('tensorflow')
install('pandoc')
install('nest_asyncio')
install('Pillow')
install('uvicorn')
install('typing_extensions', '4.7.1')
install('ipython')
