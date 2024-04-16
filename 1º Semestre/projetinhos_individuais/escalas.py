maior_menor = input("É uma escala [M]aior ou [m]enor? ")
escala = input("Digite a tônica natural da escala: ")

if maior_menor == "m":
    tipo = input("É uma escala menor [n]atural, [h]armônica ou [m]elódica? ")
    if tipo == "n":
        if escala == "C" or escala == "c":
            print("""
            A escala de Dó Menor é composta por:
            Dó - Ré - Mib - Fá - Sol - Láb - Sib
            Sua escala relativa é Mib Maior.
            """)
        elif escala == "D" or escala == "d":
            print("""
            A escala de Ré Menor é composta por:
            Ré - Mi - Fá - Sol - Lá - Sib - Dó
            Sua escala relativa é Fá Maior.
            """)
        elif escala == "E" or escala == "e":
            print("""
            A escala de Mi Menor é composta por:
            Mi - Fá# - Sol - Lá - Si - Dó - Ré
            Sua escala relativa é Sol Maior.
            """)
        elif escala == "F" or escala == "f":
            print("""
            A escala de Fá Menor é composta por:
            Fá - Sol - Láb - Sib - Dó - Réb - Mib
            Sua escala relativa é Láb Maior.
            """)
        elif escala == "G" or escala == "g":
            print("""
            A escala de Sol Menor é composta por:
            Sol - Lá - Sib - Dó - Ré - Mib - Fá
            Sua escala relativa é Sib Maior.
            """)
        elif escala == "A" or escala == "a":
            print("""
            A escala de Lá Menor é composta por:
            Lá - Si - Dó - Ré - Mi - Fá - Sol
            Sua escala relativa é Dó Maior.
            """)
        elif escala == "B" or escala == "b":
            print("""
            A escala de Si Menor é composta por:
            Si - Dó# - Ré - Mi - Fá# - Sol - Lá
            Sua escala relativa é Ré Maior.
            """)
    if tipo == "h":
        if escala == "C" or escala == "c":
            print("""
            A escala de Dó Menor Harmônica é composta por:
            Dó - Ré - Mib - Fá - Sol - Láb - Si
            """)
        elif escala == "D" or escala == "d":
            print("""
            A escala de Ré Menor Harmônica é composta por:
            Ré - Mi - Fá - Sol - Lá - Sib - Dó#
            """)
        elif escala == "E" or escala == "e":
            print("""
            A escala de Mi Menor Harmônica é composta por:
            Mi - Fá# - Sol - Lá - Si - Dó - Ré#
            """)
        elif escala == "F" or escala == "f":
            print("""
            A escala de Fá Menor Harmônica é composta por:
            Fá - Sol - Láb - Sib - Dó - Réb - Mi
            """)
        elif escala == "G" or escala == "g":
            print("""
            A escala de Sol Menor Harmônica é composta por:
            Sol - Lá - Sib - Dó - Ré - Mib - Fá#
            """)
        elif escala == "A" or escala == "a":
            print("""
            A escala de Lá Menor Harmônica é composta por:
            Lá - Si - Dó - Ré - Mi - Fá - Sol#
            """)
        elif escala == "B" or escala == "b":
            print("""
            A escala de Si Menor Harmônica é composta por:
            Si - Dó# - Ré - Mi - Fá# - Sol - Lá#
            """)
    if tipo == "m":
        if escala == "C" or escala == "c":
            print("""
            A escala de Dó Menor Melódica é composta por:
            Dó - Ré - Mib - Fá - Sol - Lá - Si
            """)
        elif escala == "D" or escala == "d":
            print("""
            A escala de Ré Menor Melódica é composta por:
            Ré - Mi - Fá - Sol - Lá - Si - Dó#
            """)
        elif escala == "E" or escala == "e":
            print("""
            A escala de Mi Menor Melódica é composta por:
            Mi - Fá# - Sol - Lá - Si - Dó# - Ré#
            """)
        elif escala == "F" or escala == "f":
            print("""
            A escala de Fá Menor Melódica é composta por:
            Fá - Sol - Láb - Sib - Dó - Ré - Mi
            """)
        elif escala == "G" or escala == "g":
            print("""
            A escala de Sol Menor Melódica é composta por:
            Sol - Lá - Sib - Dó - Ré - Mi - Fá#
            """)
        elif escala == "A" or escala == "a":
            print("""
            A escala de Lá Menor Melódica é composta por:
            Lá - Si - Dó - Ré - Mi - Fá# - Sol
            """)
        elif escala == "B" or escala == "b":
            print("""
            A escala de Si Menor Melódica é composta por:
            Si - Dó# - Ré - Mi - Fá# - Sol# - Lá#
            """)

if maior_menor == "M":
    if escala == "C" or escala == "c":
        print("""
        A escala de Dó Maior é composta por:
        Dó - Ré - Mi - Fá - Sol - Lá - Si
        Sua escala relativa é Lá Menor.
        """)
    elif escala == "D" or escala == "d":
        print("""
        A escala de Ré Maior é composta por:
        Ré - Mi - Fá# - Sol - Lá - Si - Dó#
        Sua escala relativa é Si Menor.
        """)
    elif escala == "E" or escala == "e":
        print("""
        A escala de Mi Maior é composta por:
        Mi - Fá# - Sol# - Lá - Si - Dó# - Ré#
        Sua escala relativa é Dó# Menor.
        """)
    elif escala == "F" or escala == "f":
        print("""
        A escala de Fá Maior é composta por:
        Fá - Sol - Lá - Sib - Dó - Ré - Mi
        Sua escala relativa é Ré Menor.
        """)
    elif escala == "G" or escala == "g":
        print("""
        A escala de Sol Maior é composta por:
        Sol - Lá - Si - Dó - Ré - Mi - Fá#
        Sua escala relativa é Mi Menor.
        """)
    elif escala == "A" or escala == "a":
        print("""
        A escala de Lá Maior é composta por:
        Lá - Si - Dó# - Ré - Mi - Fá# - Sol#
        Sua escala relativa é Fá# Menor.
        """)
    elif escala == "B" or escala == "b":
        print("""
        A escala de Si Maior é composta por:
        Si - Dó# - Ré# - Mi - Fá# - Sol# - Lá#
        Sua escala relativa é Sol# Menor.
        """)
