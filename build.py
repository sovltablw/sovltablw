from pathlib import Path
import shutil
src=Path('src'); dst=Path('dist')
if dst.exists(): shutil.rmtree(dst)
shutil.copytree(src,dst)
print('BUILD_OK',len(list(dst.rglob('*'))))
