"""
Process the JSON file named univ.json. Create 3 maps per instructions below.
The size of the point on the map should be based on the size of total enrollment. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons (refer to valueLabels.csv file)
The school name and the specific map criteria should be displayed when you hover over it.
(For example for Map 1, when you hover over Baylor, it should display "Baylor University, 81%")
Choose appropriate tiles for each map.


Map 1) Graduation rate for Women is over 50%
Map 2) Percent of total enrollment that are Black or African American over 10%
Map 3) Total price for in-state students living off campus over $50,000

"""
import json

infile = open("univ.json", "r")
outfile = open("readable_univ.json", "w")


univ_data = json.load(infile)

json.dump(univ_data, outfile, indent=4)


list_of_all_unis = univ_data
# print(len(list_of_unis))

conferences = [102, 108, 107, 127, 130]
sizes, lons, lats, hover_texts = [], [], [], []
schools = []

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

""" Graduation Rate - Women """
for school in list_of_all_unis:
    r = int(
        0
        if school["Graduation rate  women (DRVGR2020)"] is None
        else school["Graduation rate  women (DRVGR2020)"]
    )

    if (school["NCAA"]["NAIA conference number football (IC2020)"] in conferences) and (
        r > 50
    ):

        schools.append(school)

for uni in schools:
    rates = []
    size = uni["Total  enrollment (DRVEF2020)"]
    rate = uni["Graduation rate  women (DRVGR2020)"]
    lon = uni["Longitude location of institution (HD2020)"]
    lat = uni["Latitude location of institution (HD2020)"]
    title = uni["instnm"]
    sizes.append(size)
    rates.append(rate)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(f"{title}, {rate}%")

    data = [
        {
            "type": "scattergeo",
            "lon": lons,
            "lat": lats,
            "text": hover_texts,
            "marker": {
                "size": [size / 2500 for size in sizes],
                "color": sizes,
                "colorscale": "Viridis",
                "reversescale": True,
                "colorbar": {"title": "Total Enrollment"},
            },
        }
    ]

my_layout = Layout(title="Schools by Female Graduation Rate")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="graduation_rates_women.html")

"""Percent of Total Enrollment Black or African American"""

for school in list_of_all_unis:
    r = int(
        0
        if school[
            "Percent of total enrollment that are Black or African American (DRVEF2020)"
        ]
        is None
        else school[
            "Percent of total enrollment that are Black or African American (DRVEF2020)"
        ]
    )

    if (school["NCAA"]["NAIA conference number football (IC2020)"] in conferences) and (
        r > 10
    ):

        schools.append(school)

for uni in schools:
    rates = []
    size = uni["Total  enrollment (DRVEF2020)"]
    rate = uni[
        "Percent of total enrollment that are Black or African American (DRVEF2020)"
    ]
    lon = uni["Longitude location of institution (HD2020)"]
    lat = uni["Latitude location of institution (HD2020)"]
    title = uni["instnm"]
    sizes.append(size)
    rates.append(rate)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(f"{title}, {rate}%")

    data = [
        {
            "type": "scattergeo",
            "lon": lons,
            "lat": lats,
            "text": hover_texts,
            "marker": {
                "size": [size / 2500 for size in sizes],
                "color": sizes,
                "colorscale": "Viridis",
                "reversescale": True,
                "colorbar": {"title": "Total Enrollment"},
            },
        }
    ]

my_layout = Layout(
    title="Schools by Percent of Total Enrollment - Black or African American"
)

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="african_american_enrollment.html")

""" Total price, in-state students living off campus"""
for school in list_of_all_unis:
    r = int(
        0
        if school[
            "Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"
        ]
        is None
        else school[
            "Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"
        ]
    )

    if (school["NCAA"]["NAIA conference number football (IC2020)"] in conferences) and (
        r > 50000
    ):

        schools.append(school)

for uni in schools:
    rates = []
    size = uni["Total  enrollment (DRVEF2020)"]
    rate = uni[
        "Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"
    ]
    lon = uni["Longitude location of institution (HD2020)"]
    lat = uni["Latitude location of institution (HD2020)"]
    title = uni["instnm"]
    sizes.append(size)
    rates.append(rate)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(f"{title}, ${rate}")

    data = [
        {
            "type": "scattergeo",
            "lon": lons,
            "lat": lats,
            "text": hover_texts,
            "marker": {
                "size": [size / 2500 for size in sizes],
                "color": sizes,
                "colorscale": "Viridis",
                "reversescale": True,
                "colorbar": {"title": "Total Enrollment"},
            },
        }
    ]

my_layout = Layout(title="Schools by Price - Off-Campus In-State Students")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="instate_cost.html")
