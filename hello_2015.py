def fuck(hhh):print(hhh);
def fuckIn(hhh):return chr(hhh);
a=[0,0,0,0];tmp=[0,0,0,0];c=[0,0,0,0];r=0;
for i in range(0,4):
    if i==0 :r=2;
    if i>=1 and i<=2:r+=0.5;
    a[i]=r;
a[3]+=1.5;i=0;
for j in a:
    j*=2;a[i]=int(j);i+=1;
a.insert(0,44);tmp=a.copy();
a[1]=a[0]+tmp[3];a[2]=a[0]+tmp[1];
a[3]=a[0]+tmp[2];a[4]=a[0]+tmp[4];
tmp[0]=3;
for i in range(0,4):
    if i>0 and i<=1:tmp[i]=3;
    if i>=2 and i<3:tmp[i]=tmp[i-1]*tmp[i-1]+1;
    if i<4 and i>=3:tmp[i]=tmp[i-2]*(tmp[i-1]-2)+5;
tmp[4]=111;j=0;k=3;
c=tmp.copy();
for i in tmp:
    tmp[j]=tmp[4]-c[k];
    j+=1;k-=1;
tmp[4]=111;tmp[0]-=c[2];
for i in a:
    tmp.append(i);
ass=tmp;
bitch='';
for shit in ass:
    bitch+=fuckIn(shit);
fuck(bitch);
