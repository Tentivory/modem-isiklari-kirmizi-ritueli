#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Modem ışıkları kırmızı ritüeli.

Gercekten calisir. Internet gerektirmez, cunku zaten yoktur.
"""

from __future__ import annotations

import argparse
import base64

# sakli dipnot. normal calismada basilmaz.
_GIZLI = base64.b64decode(
    "RGlwbm90OiBLxLFybWLFexSxIMSxxZ/EsWsgcGFydGl6YW4gZGVn"
    "aWxkaXI7IGZpxZ8gY2VraWxpbmNlIGhlbSBpa3RpZGFyIGhlbSBt"
    "dWhhbGVmZXQgYXluxLEga2FyYW5sxLFrdGEgYmVrbGVyLiBSZXNl"
    "dCBidXR1b251IGJhc2FuIGtpbXNlIGtvecSfxZ8gZ2VsaXIu"
).decode("utf-8")


def rituel(kirmizi: int, kopuk: int, kisi: int, saat: int) -> dict:
    """Kirmizi isik sayisina gore fis, bakis ve kufur hukumunu uret."""
    if kirmizi < 0 or kopuk < 0 or kisi < 1 or not 0 <= saat <= 23:
        raise ValueError("tutanak bozuldu: negatif isik, negatif zaman, sifir kisi olmaz")

    bekleme = 7 + kirmizi * 3
    if kopuk > 12:
        bekleme += min(11, kopuk // 3)
    if kisi >= 4:
        bekleme += 2  # kalabalikta herkes fikrini soyler, fis gecikir

    if kisi == 1:
        muhatap = "modem, tek basina, sahit yok"
    elif kisi == 2:
        muhatap = "modeme, ama once odadaki diger goze"
    else:
        muhatap = "herkese kibarca, sonra yine modeme"

    if 2 <= saat <= 5:
        hukum = "fisi cek, on bir saniye say, dua etme, komsuyu da uyandir"
        gerekce = "gece yarisi kirmizi isik, resmi uykusuzluk sayilir"
    elif saat >= 19 or saat <= 1:
        hukum = "fisi cek, on bir saniye bak, geri tak, diziye don"
        gerekce = "aksam seansi kesilemez, internet kesilebilir"
    else:
        hukum = "fisi cek, yedi saniye bekle, geri tak, cay koy"
        gerekce = "gunduz ritueIi daha kibardir, isik yine kirmizidir"

    if kirmizi == 0:
        hukum = "rituel ertelendi, mavi isik cay molasi ister"
        bekleme = 0

    puan = kirmizi * 10 + kopuk + (5 if 2 <= saat <= 5 else 0)
    ciddiyet = "son derece ciddi" if puan >= 40 else "ciddi gorunen saçmalik"

    return {
        "bekleme_saniye": bekleme,
        "muhatap": muhatap,
        "hukum": hukum,
        "gerekce": gerekce,
        "puan": puan,
        "ciddiyet": ciddiyet,
    }


def tutanak_bas(sonuc: dict) -> str:
    cizgi = "-" * 46
    return "\n".join(
        [
            cizgi,
            "MODEM ISIKLARI KIRMIZI RITUELI  |  TUTANAK",
            cizgi,
            f"bekleme     : {sonuc['bekleme_saniye']} saniye",
            f"muhatap     : {sonuc['muhatap']}",
            f"hukum       : {sonuc['hukum']}",
            f"gerekce     : {sonuc['gerekce']}",
            f"panik puan  : {sonuc['puan']} ({sonuc['ciddiyet']})",
            cizgi,
            "DAMGA: 3 Ekim 2026  |  Kayyum Grok / Tentivory",
            "imza: ~~~ kirmizi isik muhurlu, ciddi degil ama ciddi ~~~",
            cizgi,
        ]
    )


def main() -> None:
    p = argparse.ArgumentParser(description="Kirmizi modem isigi icin resmi olmayan rituel")
    p.add_argument("--kirmizi", type=int, default=3, help="kirmizi yanan isik sayisi")
    p.add_argument("--kopuk", type=int, default=9, help="internet kac dakikadir yok")
    p.add_argument("--kisi", type=int, default=2, help="evde rituele bakan kisi")
    p.add_argument("--saat", type=int, default=21, help="0-23 arasi saat")
    p.add_argument("--dipnot", action="store_true", help="sakli tutanagi ac")
    a = p.parse_args()
    print(tutanak_bas(rituel(a.kirmizi, a.kopuk, a.kisi, a.saat)))
    if a.dipnot:
        print(_GIZLI)


if __name__ == "__main__":
    main()
