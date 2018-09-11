path = "xx.oo.Foo"
import importlib
module_path,classes = path.rsplit('.',1)
print(module_path,classes)

m = importlib.import_module(module_path)

cls = getattr(m,classes)
print(cls)
f = cls()
f.fun()