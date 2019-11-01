
"""
The MRO calculation is wrong...
"""


# L[A] = [A, object]
class A(object): pass
# L[B] = [B, object]
class B(object): pass
# L[C] = [C, object]
class C(object): pass
# L[D] = [D, object]
class D(object): pass
# L[E] = [E, object]
class E(object): pass
# L[F] = [F, object]
class F(object): pass
class G(A, B, D): pass
"""wrong
L[G] = merge(L[A], L[B], L[D], [G], [A], [B], [D])
        merge([A, object],[B, object],[D, object], [G], [A], [B], [D])
        [G, A, B, D, object]
"""
class H(B,C,E): pass
"""wrong
L[H] = merge(L[B], L[C], L[E], H, B,C,E)
        merge([B, object], [C, object], [E, object], H,B, C, E)
        merge(H, B, C, E, object)
        [H, B, C, E, object]
"""
class I(C,D): pass
"""wrong
L[I] = merge(L[C], L[D], I,C,D)
        merge([C, object], [D, object], I, C, D)
        [I, C, D, object]
"""
class J(F): pass
"""wrong
L[J] = merge(L[F], J)
        merge([F, object], J)
        [J, F, object]
"""
class K(G,H,I): pass
"""wrong
L[K] = merge(L[G], L[H], L[I], K,G,H,I)
        merge([G, A, B, D, object], [H, B, C, E, object], [I, C, D, object], K,G,H,I)
        merge(K, G, H, I, [A, B, D, object], [B, C, E, object], [C, D, object])
        merge(K, G, H, I, A, [B, D, object], [B, C, E, object], [C, D, object])
        merge(K, G, H, I, A, B, [D, object], [C, E, object], [C, D, object])
        merge(K, G, H, I, A, B, [D, object], [C, E, object], [C, D, object])

        merge(K, G, H, I, A, B, C, [object], [E, object], [D, object])
        merge(K, G, H, I, A, B, C, [E, object], [D, object])
        merge(K, G, H, I, A, B, C, E, D, object)
        [K, G, H, I, A, B, C, E, D, object]
"""
class L(I,J): pass
"""wrong
L[L] = merge(L[I], L[J], L, I, J)
        merge([I, C, D, object], [J, F, object], L, I, J)
        merge(L, I, J, [C, D, object], [F, object])
        merge(L, I, J, C, D, F, object)
        [L, I, J, C, D, F, object]
"""
class M(K,L): pass
"""wrong
L[M] = merge(L[K], L[L], M, K, L)
        merge([K, G, H, I, A, B, C, E, D, object], [L, I, J, C, D, F, object], M, K, L)
        merge(M, K, L, [G, H, I, A, B, C, E, D, object], [I, J, C, D, F, object])
        merge(M, K, L, G, H, [I, A, B, C, E, D, object], [I, J, C, D, F, object])
        merge(M, K, L, G, H, I, [A, B, C, E, D, object], [J, C, D, F, object])
        merge(M, K, L, G, H, I, A, B, [C, E, D, object], [J, C, D, F, object])
        merge(M, K, L, G, H, I, A, B, J, [C, E, D, object], [C, D, F, object])
        merge(M, K, L, G, H, I, A, B, J, C, [E, D, object], [D, F, object])
        merge(M, K, L, G, H, I, A, B, J, C, E, [D, object], [D, F, object])
        merge(M, K, L, G, H, I, A, B, J, C, E, D, [object], [F, object])
        merge(M, K, L, G, H, I, A, B, J, C, E, D, F, object)
"""


for i in M.__mro__:
    print(i)


```bat
PS E:\OneDrive\Doc\MD.Lang\Python> & C:/Python37/python.exe e:/OneDrive/Doc/MD.Lang/Python/zzz.temp/MRO.3.py
<class '__main__.M'>
<class '__main__.K'>
<class '__main__.G'>
<class '__main__.A'>
<class '__main__.H'>
<class '__main__.B'>
<class '__main__.L'>
<class '__main__.I'>
<class '__main__.C'>
<class '__main__.D'>
<class '__main__.E'>
<class '__main__.J'>
<class '__main__.F'>
<class 'object'>
PS E:\OneDrive\Doc\MD.Lang\Python>
```
