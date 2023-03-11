from restapi.app.models import *

DELTA_CLO = .5

def get_user_recomendations(user_id, wr: WeatherRecord):
    user = User.objects.get(id=user_id)

    jackets = (
        ClothItem.objects.all()
        .filter(user=user)
        .filter(type=ClothItem.ClothTypes.JACKET)
        .order_by("thermal_resistance_min")
    )
    shirts = (
        ClothItem.objects.all()
        .filter(user=user)
        .filter(type=ClothItem.ClothTypes.SHIRTS)
        .order_by("thermal_resistance_min")
    )
    shoes = (
        ClothItem.objects.all()
        .filter(user=user)
        .filter(type=ClothItem.ClothTypes.SHOES)
        .order_by("thermal_resistance_min")
    )
    socks = (
        ClothItem.objects.all()
        .filter(user=user)
        .filter(type=ClothItem.ClothTypes.SOCKS)
        .order_by("thermal_resistance_min")
    )
    headgears = (
        ClothItem.objects.all()
        .filter(user=user)
        .filter(type=ClothItem.ClothTypes.HEADGEAR)
        .order_by("thermal_resistance_min")
    )
    pants = (
        ClothItem.objects.all()
        .filter(user=user)
        .filter(type=ClothItem.ClothTypes.PANTS)
        .order_by("thermal_resistance_min")
    )
    clo = wr.calculate_CLO()

    tops = []
    for j in jackets:
        for s in shirts:
            if abs(s.thermal_resistance_mean - clo) < abs(s.thermal_resistance_mean - s.thermal_resistance_max) * 2:
                tops.append((s.name, ""))
            if abs(j.thermal_resistance_mean + s.thermal_resistance_mean - clo) < (abs(j.thermal_resistance_mean - j.thermal_resistance_max) + abs(s.thermal_resistance_mean - s.thermal_resistance_max)) * 2:
                tops.append((j.name, s.name))

    feets = []
    for sck in socks:
        for sh in shoes:
            if abs(sck.thermal_resistance_mean + sh.thermal_resistance_mean - clo) < (abs(sck.thermal_resistance_mean - sck.thermal_resistance_max) + abs(sh.thermal_resistance_mean - sh.thermal_resistance_max)) * 2:
                feets.append((sck.name, sh.name))

    bottoms = []
    for p in pants:
        if abs(p.thermal_resistance_mean - clo) < abs(p.thermal_resistance_mean - p.thermal_resistance_max) * 2:
            bottoms.append((p.name, ""))

    heads = []
    for h in headgears:
        if abs(h.thermal_resistance_mean - clo) < abs(h.thermal_resistance_mean - h.thermal_resistance_max) * 2:
            heads.append((h.name, ""))

    return {
        "tops": tops,
        "bottoms": bottoms,
        "heads": heads,
        "feets": feets
    }