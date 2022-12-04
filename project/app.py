import geopandas
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd
from pandas_datareader import wb
from shiny import App, render, ui
from statsmodels.formula.api import ols

plt.rcParams['figure.figsize'] = (10.0, 10.0)

# dateset 1
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world['world_pop_share'] = world['pop_est'] / sum(world['pop_est'])
fig, ax = plt.subplots()
continent_df = world[['pop_est', 'continent']].groupby(by='continent').sum()

# dateset 2
country = ['CAN', 'USA', 'CHN', 'JPN', 'GRC', 'FRA', 'PER', 'CHL', 'NGA', 'MOZ']
df = wb.download(indicator='EN.POP.DNST', country=country, start=1970, end=2000)
df = df.rename(columns={'EN.POP.DNST': 'population'}).sort_index()

# dataset3
us_pd = pd.read_csv("us-counties.csv")
fig, ax = plt.subplots()
sum_pd = us_pd.groupby(by='date').sum()

# Analysis with OLS model
reset_index_df = df.reset_index()
pivot_df = pd.pivot(reset_index_df, index="year", columns="country", values="population")
sort_pivot_df = pivot_df.sort_index().reset_index()
sort_pivot_df['year'] = sort_pivot_df['year'].astype('int')
prestige_model = ols("China~year", data=sort_pivot_df).fit()
print(prestige_model.summary())

app_ui = ui.page_fluid(
    ui.row(ui.h2("Population World and Country", align="center")),
    ui.row(ui.input_switch(id="world", label="Show World Population ", value="True")),
    ui.row(ui.input_select("country", "Choose country to show",
                           {"Canada": "Canada", "United States": "United States", "China": "China", "Japan": "Japan"})),
    ui.row(ui.output_plot("show"), align="center"),
    ui.row(ui.output_plot("init_epidemic"), align="center"),
    ui.row(ui.output_plot("pop_contient"), align="center"))


def server(input, output, session):
    @output
    @render.plot
    def show():
        fig, ax = plt.subplots(figsize=(8, 8))
        if input.world():
            world[world.continent != 'Antarctica'].plot(ax=ax, column='world_pop_share', legend=True)
            ax.axis('off')
            ax.set_title('Share of World Population')
            return ax
        else:
            cname = input.country()
            c = df.loc[cname]
            ax.plot(c.index, c['population'])
            ax.set_title('Population of ' + cname)
            return ax

    @output
    @render.plot
    def init_epidemic():
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.plot(sum_pd)
        ax.set_title('Analysis of the U.S. Epidemic')
        tick_spacing_ = sum_pd.index.size / 3
        ax.xaxis.set_major_locator(mticker.MultipleLocator(tick_spacing_))
        return ax

    @output
    @render.plot
    def pop_contient():
        ax.bar(continent_df.index, continent_df['pop_est'], width=1, edgecolor="white", linewidth=0.7)
        tick_spacing_pop = continent_df.index.size / 5
        ax.xaxis.set_major_locator(mticker.MultipleLocator(tick_spacing_pop))
        return ax


app = App(app_ui, server)
