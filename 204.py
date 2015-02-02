class Meta:
    def __getattr__(self,name):
        print(name)

meta=Meta()
meta.a
meta.b=2n
print(meta.b)
