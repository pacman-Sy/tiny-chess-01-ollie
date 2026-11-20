import json,os,random,sys,urllib.request as w
U0=os.environ["MAKEFUN_ENV_URL"]
MATE=30000;INF=31000
MG=[100,350,350,500,1000,0];EG=[100,300,300,500,950,0]
MGP=[0,0,0,0,0,0,0,0,100,150,50,100,50,150,50,0,0,0,50,50,50,50,0,0,0,0,0,0,0,0,0,0,-50,0,0,0,0,0,0,0,-50,0,0,0,0,0,50,0,-50,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0]
EGP=[0,0,0,0,0,0,0,0,200,150,150,150,150,150,150,200,100,100,100,50,50,50,100,100,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
MGN=[-150,-100,-50,-50,50,-100,0,-100,-50,-50,50,50,0,50,0,0,-50,50,50,50,100,150,50,50,0,0,0,50,50,50,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,-50,-50,0,0,0,0,0,0,-100,0,-50,-50,0,-50,0,0]
EGN=[-50,-50,0,-50,-50,-50,-50,-100,0,0,0,0,0,0,0,-50,0,0,0,0,0,0,0,-50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-50,0,0,0,0,0,0,-50,-50,-50,0,0,0,0,-50,-50]
MGB=[-50,0,-100,-50,0,-50,0,0,-50,0,0,0,50,50,0,-50,0,50,50,50,50,50,50,0,0,0,0,50,50,50,0,0,0,0,0,50,50,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,50,0,-50,0,0,0,0,0,-50,0]
EGB=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-50,0,0,0,0,0,0,0,0]
MGR=[50,50,50,50,50,0,50,50,50,50,50,50,100,50,50,50,0,0,50,50,0,50,50,0,0,0,0,50,0,50,0,0,-50,-50,0,0,0,0,0,0,-50,0,0,0,0,0,0,-50,-50,0,0,0,0,0,0,-50,0,0,0,0,0,0,-50,-50]
EGR=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
MGQ=[-50,0,50,0,50,50,50,50,0,-50,0,0,0,50,50,50,0,0,0,0,50,50,50,50,-50,-50,0,0,0,0,0,0,0,-50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-50,0,0,0,0,0,0,0,0,0,0,0,0,0,-50,-50]
EGQ=[0,0,0,50,50,0,0,0,0,0,50,50,50,0,50,0,0,0,0,50,50,50,0,0,0,0,0,50,50,50,50,50,0,50,0,50,50,50,50,0,0,-50,0,0,0,0,0,0,0,0,-50,0,0,0,-50,-50,-50,-50,0,-50,0,-50,0,-50]
MGK=[-50,0,0,0,-50,-50,0,0,50,0,0,0,0,0,-50,-50,0,0,0,0,0,0,0,0,0,0,0,-50,-50,0,0,-50,-50,0,-50,-50,-50,-50,-50,-50,0,0,0,-50,-50,-50,0,-50,0,0,0,-50,-50,0,0,0,0,50,0,-50,0,-50,0,0]
EGK=[-50,-50,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,50,50,0,0,0,0,50,50,50,50,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,-50,0,0,0,0,0,0,0,-50,-50,0,0,-50,0,0,-50]
TB=[MGP,MGN,MGB,MGR,MGQ,MGK];TE=[EGP,EGN,EGB,EGR,EGQ,EGK]
PT=[0]*2048;PE=[0]*2048;VAL=[0]*16;PH=[0]*16
for t in range(6):
    VAL[t+1]=MG[t];VAL[t+9]=-MG[t]
    PH[t+1]=0 if t==0 else 1 if t<3 else 2 if t==3 else 4 if t==4 else 0
    PH[t+9]=PH[t+1]
    for s in range(128):
        if s&0x88:continue
        r=s>>4;f=s&7
        PT[(t+1)*128+s]=MG[t]+TB[t][(7-r)*8+f]
        PE[(t+1)*128+s]=EG[t]+TE[t][(7-r)*8+f]
        PT[(t+9)*128+s]=-(MG[t]+TB[t][r*8+f])
        PE[(t+9)*128+s]=-(EG[t]+TE[t][r*8+f])
F=[0x0101010101010101<<f for f in range(8)]
WP=[0]*64;BP=[0]*64
for r in range(8):
    for f in range(8):
        m=0
        for rr in range(r+1,8):
            for ff in range(max(f-1,0),min(f+1,7)+1):m|=1<<(rr*8+ff)
        WP[r*8+f]=m
        m=0
        for rr in range(r):
            for ff in range(max(f-1,0),min(f+1,7)+1):m|=1<<(rr*8+ff)
        BP[r*8+f]=m
PB=[0,6,12,20,34,56,90,0]
R=random.Random(20261120).getrandbits
ZP=[R(64) for _ in range(2048)];ZS=R(64);ZC=[R(64) for _ in range(16)];ZE=[R(64) for _ in range(8)]
ND=(-33,-31,-18,-14,14,18,31,33);KD=(-17,-16,-15,-1,1,15,16,17)
BD=(-17,-15,15,17);RD=(-16,-1,1,16)
KP=[15]*128
KP[0]=13;KP[7]=14;KP[4]=12;KP[112]=7;KP[119]=11;KP[116]=3
B=[0]*128;SIDE=0;CAST=0;EP=-1;HALF=0;H=0;M=0;E=0;PHS=0
OCC=[0,0];PWN=[0,0];KING=[4,116];U=[];TT={};KL=[(0,0)]*99;NODES=0;LMT=0

def c64(s):return (s>>4)*8+(s&7)
def c128(i):return (i>>3)*16+(i&7)
def atk(sq,by):
    b=B
    if by:
        t=sq+15
        if not t&0x88 and b[t]==9:return 1
        t=sq+17
        if not t&0x88 and b[t]==9:return 1
    else:
        t=sq-15
        if not t&0x88 and b[t]==1:return 1
        t=sq-17
        if not t&0x88 and b[t]==1:return 1
    n=2+by*8
    for d in ND:
        t=sq+d
        if not t&0x88 and b[t]==n:return 1
    k=6+by*8
    for d in KD:
        t=sq+d
        if not t&0x88 and b[t]==k:return 1
    r=4+by*8;q=5+by*8;bi=3+by*8
    for d in RD:
        t=sq+d
        while not t&0x88:
            p=b[t]
            if p:
                if p==r or p==q:return 1
                break
            t+=d
    for d in BD:
        t=sq+d
        while not t&0x88:
            p=b[t]
            if p:
                if p==bi or p==q:return 1
                break
            t+=d
    return 0

def load(fen):
    global B,SIDE,CAST,EP,HALF,H,M,E,PHS,OCC,PWN,KING
    B=[0]*128
    ps=fen.split();rows=ps[0].split("/")
    for ri,row in enumerate(rows):
        f=0
        for ch in row:
            if ch.isdigit():f+=int(ch)
            else:
                B[(7-ri)*16+f]={"p":1,"n":2,"b":3,"r":4,"q":5,"k":6}[ch.lower()]+(0 if ch.isupper() else 8);f+=1
    SIDE=0 if ps[1]=="w" else 1
    CAST=0
    if "K" in ps[2]:CAST|=1
    if "Q" in ps[2]:CAST|=2
    if "k" in ps[2]:CAST|=4
    if "q" in ps[2]:CAST|=8
    EP=-1
    if ps[3]!="-":EP=(int(ps[3][1])-1)*16+ord(ps[3][0])-97
    HALF=int(ps[4]) if len(ps)>4 else 0
    OCC=[0,0];PWN=[0,0];KING=[-1,-1];M=0;E=0;PHS=0;H=0
    for sq in range(128):
        pc=B[sq]
        if not pc or sq&0x88:continue
        c=pc>>3;i=c64(sq)
        OCC[c]|=1<<i
        if pc&7==1:PWN[c]|=1<<i
        if pc&7==6:KING[c]=sq
        M+=PT[pc*128+sq];E+=PE[pc*128+sq];PHS+=PH[pc]
        H^=ZP[pc*128+sq]
    if SIDE:H^=ZS
    H^=ZC[CAST]
    if EP>=0:H^=ZE[EP&7]

def gen(caps):
    o=[];b=B;us=SIDE;th=us^1;ep=EP;bb=OCC[us]
    while bb:
        lo=bb&-bb;bb^=lo
        f=c128(lo.bit_length()-1);pc=b[f];t=pc&7
        if t==1:
            fwd=16 if not us else -16;r=f>>4;one=f+fwd
            if not b[one]:
                if r==(6 if not us else 1):
                    for pr in (5,4,3,2):o.append(f|one<<7|pr<<14)
                elif not caps:
                    o.append(f|one<<7)
                    if r==(1 if not us else 6) and not b[one+fwd]:o.append(f|(one+fwd)<<7|8<<17)
            for d in (fwd-1,fwd+1):
                to=f+d
                if to&0x88:continue
                q=b[to]
                if q and q>>3==th:
                    if r==(6 if not us else 1):
                        for pr in (5,4,3,2):o.append(f|to<<7|pr<<14|1<<17)
                    else:o.append(f|to<<7|1<<17)
                elif to==ep:o.append(f|to<<7|1<<17|2<<17)
            continue
        if t==2:
            for d in ND:
                to=f+d
                if to&0x88:continue
                q=b[to]
                if not q:
                    if not caps:o.append(f|to<<7)
                elif q>>3==th:o.append(f|to<<7|1<<17)
            continue
        if t==6:
            for d in KD:
                to=f+d
                if to&0x88:continue
                q=b[to]
                if not q:
                    if not caps:o.append(f|to<<7)
                elif q>>3==th:o.append(f|to<<7|1<<17)
            if not caps and not atk(f,th):
                base=0 if not us else 112
                c1=1 if not us else 4;c2=2 if not us else 8
                if CAST&c1 and not b[base+5] and not b[base+6] and not atk(base+5,th) and not atk(base+6,th):o.append(f|(base+6)<<7|4<<17)
                if CAST&c2 and not b[base+1] and not b[base+2] and not b[base+3] and not atk(base+3,th) and not atk(base+2,th):o.append(f|(base+2)<<7|4<<17)
            continue
        dirs=BD if t==3 else RD if t==4 else KD
        for d in dirs:
            to=f+d
            while not to&0x88:
                q=b[to]
                if not q:
                    if not caps:o.append(f|to<<7)
                else:
                    if q>>3==th:o.append(f|to<<7|1<<17)
                    break
                to+=d
    return o

def mk(m,inchk):
    global SIDE,CAST,EP,HALF,H,M,E,PHS,OCC,PWN,KING
    f=m&127;to=(m>>7)&127;pr=(m>>14)&7;fl=(m>>17)&15
    pc=B[f];us=pc>>3;th=us^1
    csq=to
    if fl&2:csq=to-16 if not us else to+16
    cap=B[csq]
    U.append((m,pc,cap,CAST,EP,HALF,H,M,E,PHS,OCC[0],OCC[1],PWN[0],PWN[1],KING[0],KING[1]))
    h=H;mg=M;eg=E;ph=PHS;occ=OCC;pwn=PWN
    if cap:
        B[csq]=0;ci=c64(csq);occ[th]^=1<<ci
        if cap&7==1:pwn[th]^=1<<ci
        mg-=PT[cap*128+csq];eg-=PE[cap*128+csq];ph-=PH[cap];h^=ZP[cap*128+csq]
    B[f]=0;fi=c64(f);occ[us]^=1<<fi
    if pc&7==1:pwn[us]^=1<<fi
    mg-=PT[pc*128+f];eg-=PE[pc*128+f];ph-=PH[pc];h^=ZP[pc*128+f]
    pl=pc if not pr else pr|us<<3
    B[to]=pl;ti=c64(to);occ[us]^=1<<ti
    if pl&7==1:pwn[us]^=1<<ti
    mg+=PT[pl*128+to];eg+=PE[pl*128+to];ph+=PH[pl];h^=ZP[pl*128+to]
    if pc&7==6:KING[us]=to
    if fl&4:
        rf=f+3 if to>f else f-4;rt=f+1 if to>f else f-1;rp=B[rf]
        B[rf]=0;B[rt]=rp
        occ[us]^=1<<c64(rf);occ[us]^=1<<c64(rt)
        mg+=PT[rp*128+rt]-PT[rp*128+rf];eg+=PE[rp*128+rt]-PE[rp*128+rf]
        h^=ZP[rp*128+rf]^ZP[rp*128+rt]
    h^=ZC[CAST];CAST&=KP[f]&KP[to];h^=ZC[CAST]
    if EP>=0:h^=ZE[EP&7]
    EP=-1
    if fl&8:
        e=(f+to)>>1
        if pwn[th]&((1<<c64(to-1))|(1<<c64(to+1))):EP=e;h^=ZE[e&7]
    HALF=0 if (pc&7==1 or cap) else HALF+1
    SIDE=th;M=mg;E=eg;PHS=ph;OCC=occ;PWN=pwn;H=h^ZS
    k=KING[us]
    if pc&7==6 or fl&4 or fl&2 or inchk or k>>4==f>>4 or (k&7)==(f&7) or (k-f)%15==0 or (k-f)%17==0:
        if atk(k,th):um();return 0
    return 1

def um():
    global SIDE,CAST,EP,HALF,H,M,E,PHS,OCC,PWN,KING
    m,pc,cap,cast,ep,half,h,mg,eg,ph,o0,o1,p0,p1,k0,k1=U.pop()
    f=m&127;to=(m>>7)&127;fl=(m>>17)&15;us=pc>>3
    B[f]=pc;B[to]=0
    if fl&2:B[to-16 if not us else to+16]=cap
    elif cap:B[to]=cap
    if fl&4:
        rf=f+3 if to>f else f-4;rt=f+1 if to>f else f-1
        B[rf]=B[rt];B[rt]=0
    SIDE=us;CAST=cast;EP=ep;HALF=half;H=h;M=mg;E=eg;PHS=ph
    OCC=[o0,o1];PWN=[p0,p1];KING=[k0,k1]

def ev():
    ph=PHS
    if ph>24:ph=24
    s=(M*ph+E*(24-ph))//24
    wp=PWN[0];bp=PWN[1];b=B
    x=wp
    while x:
        lo=x&-x;x^=lo;i=lo.bit_length()-1;r=i>>3
        if not bp&WP[i]:s+=PB[r]
    x=bp
    while x:
        lo=x&-x;x^=lo;i=lo.bit_length()-1;r=7-(i>>3)
        if not wp&BP[i]:s-=PB[r]
    return s+10 if not SIDE else -s-10

def qs(a,b,ply):
    global NODES
    NODES+=1
    if NODES>LMT:return a
    st=ev()
    if st>=b:return st
    if st>a:a=st
    sc=[]
    for m in gen(1):
        vv=VAL[B[(m>>7)&127]&15]
        if st+vv< a-200:continue
        sc.append((vv-VAL[B[m&127]&15],m))
    sc.sort(reverse=True)
    ck=atk(KING[SIDE],SIDE^1)
    for _,m in sc:
        if mk(m,ck):
            v=-qs(-b,-a,ply+1)
            um()
            if v>=b:return v
            if v>a:a=v
    return a

def order(ms,ply,hb):
    sc=[];k1,k2=KL[ply]
    for m in ms:
        to=(m>>7)&127;f=m&127
        if m==hb:v=1<<28
        elif m&(1<<17):v=(1<<20)+VAL[B[to]&15]*16-VAL[B[f]&15]
        elif m==k1:v=1<<19
        elif m==k2:v=(1<<19)-1
        elif (m>>14)&7:v=1<<18
        else:v=0
        sc.append((v,m))
    sc.sort(reverse=True)
    return sc

def ab(d,a,b,ply):
    global NODES
    NODES+=1
    if NODES>LMT:return a
    chk=atk(KING[SIDE],SIDE^1)
    if chk:d+=1
    if d<=0:return qs(a,b,ply)
    key=H
    ent=TT.get(key)
    hb=0
    if ent:
        hb=ent[2]
        if ent[0]>=d:
            v=ent[1]
            if v>MATE-200:v-=ply
            elif v<-MATE+200:v+=ply
            if ent[3]==0:return v
            if ent[3]==1 and v<=a:return v
            if ent[3]==2 and v>=b:return v
    ms=gen(0)
    if not ms:return MATE-ply if chk else 0
    best=-INF;flag=1;bm=0;a0=a;mc=0
    for _,m in order(ms,ply,hb):
        mc+=1
        r=1 if (mc>4 and not m&(1<<17) and not (m>>14)&7 and d>=3) else 0
        if mk(m,chk):
            v=-ab(d-1-r,-b,-a,ply+1)
            um()
            if NODES>LMT:return a0
            if v>best:
                best=v;bm=m
                if v>a:
                    a=v;flag=0
                    if v>=b:
                        if not m&(1<<17):KL[ply]=(m,KL[ply][0])
                        flag=2
                        break
    if best>MATE-200:best+=ply
    elif best<-MATE+200:best-=ply
    TT[key]=(d,best,bm,flag)
    return best

def cvt(m):
    f=m&127;to=(m>>7)&127;pr=(m>>14)&7
    s="abcdefgh"[f&7]+str((f>>4)+1)+"abcdefgh"[to&7]+str((to>>4)+1)
    return s+"  nbrq"[pr] if pr else s

def mv(fen,budget=45000):
    global NODES,LMT,TT,KL,U
    load(fen)
    TT={};KL=[(0,0)]*99;U=[]
    ms=gen(0)
    if not ms:return None
    best=ms[0]
    NODES=0;LMT=budget
    for d in range(1,30):
        cur=best;bs=-INF;done=1
        ck=atk(KING[SIDE],SIDE^1)
        for _,m in order(ms,0,best):
            if mk(m,ck):
                v=-ab(d-1,-INF,-bs,1)
                um()
                if NODES>LMT:done=0;break
                if v>bs:bs=v;cur=m
        if not done:break
        best=cur
    return cvt(best)

def post(p,b):
    r=w.Request(U0+p,json.dumps(b).encode(),{"content-type":"application/json"})
    with w.urlopen(r,timeout=60) as x:return json.load(x)

def run():
    while 1:
        g=post("/game",{})
        if g["status"]=="done":break
        while g["status"]=="your_move":
            m=mv(g["fen"])
            if m is None or m not in g["legal_moves"]:m=g["legal_moves"][0]
            g=post("/move",{"game":g["game"],"move":m})
    print(f"done: {g.get('wins')} {g.get('draws')} {g.get('losses')}",file=sys.stderr)

if __name__=="__main__":run()
