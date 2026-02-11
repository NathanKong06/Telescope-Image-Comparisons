import streamlit as st
from streamlit_image_comparison import image_comparison

st.set_page_config("Space Images Comparisons")

st.header("Space Images Comparisons")

st.write("")
st.write("Concepts and some images are from [WebbCompare](https://www.webbcompare.com/index.html) app by [John Christensen](https://twitter.com/JohnnyC1423) and [Streamlit](https://github.com/streamlit/example-app-image-comparison/blob/main/streamlit_app.py) but with additional images and information.")
st.write("")
st.markdown("""
**About the Telescopes**

**Hubble Space Telescope (HST)** observes primarily in visible and ultraviolet light, with limited near-infrared capability, from low Earth orbit, providing high-resolution optical views of galaxies, nebulae, and star clusters since 1990.  
**James Webb Space Telescope (JWST)** observes mainly in near- and mid-infrared wavelengths from the Sun–Earth L2 point, allowing it to see through dust and detect cooler, more distant objects in the universe.
""")

st.markdown("### Pillars of Creation")
st.write("The Pillars of Creation are towering columns of gas and dust within the Eagle Nebula (M16) where new stars are forming. Infrared observations reveal stars hidden inside the dense dust clouds that are obscured in visible light.")
image_comparison(
    img1="https://cdn.esahubble.org/archives/images/screen/heic1501a.jpg",
    img2="https://cdn.esawebb.org/archives/images/screen/weic2216e.jpg",
    label1="Hubble",
    label2="Webb",
)

st.markdown("### M101 Spiral Galaxy")
st.write("M101, also known as the Pinwheel Galaxy, is a large face-on spiral galaxy located about 21 million light-years away. This composite image combines multiple exposures from Spitzer (infrared), Hubble (optical), and Chandra (X-ray). Spitzer was retired in 2020.")
image_comparison(
    img1="https://assets.science.nasa.gov/dynamicimage/assets/science/missions/hubble/releases/2009/02/STScI-01EVT5S0014XSYMBAATA2CC769.tif?w=7200&h=7200&fit=crop&crop=faces%2Cfocalpoint",
    img2="https://assets.science.nasa.gov/dynamicimage/assets/science/missions/hubble/releases/2009/02/STScI-01F3H7CZCWP94816FTYNT4MYA9.tif?w=7200&h=7200&fit=crop&crop=faces%2Cfocalpoint",
    label1="Hubble",
    label2="Composite",
)

st.markdown("### Ring Nebula")
st.write("The Ring Nebula (M57) is a planetary nebula formed from the outer layers of a dying Sun-like star. Infrared observations reveal complex structures and molecular material beyond the bright optical ring.")
image_comparison(
    img1="https://cdn.esawebb.org/archives/images/screen/weic2320f.jpg",
    img2="https://cdn.esawebb.org/archives/images/screen/weic2320d.jpg",
    label1="Hubble",
    label2="Webb",
)

st.markdown("### Cartwheel Galaxy")
st.write("The Cartwheel Galaxy is a ring galaxy formed by a high-speed collision with a smaller galaxy. The impact triggered intense star formation visible in both optical and infrared wavelengths.")
image_comparison(
    img1="https://github.com/JohnEdChristensen/WebbCompare/blob/gh-pages/img/hubble/cartwheel_2800.png?raw=true",
    img2="https://github.com/JohnEdChristensen/WebbCompare/blob/gh-pages/img/webb/cartwheel_2800.png?raw=true",
    label1="Hubble",
    label2="Webb",
)

st.markdown("### Crab Nebula")
st.write("The Crab Nebula (M1) is a supernova remnant left behind by a stellar explosion observed in 1054 AD. The nebula is powered by a central pulsar, a rapidly rotating neutron star, which drives high-energy particle emissions. Optical images show intricate filaments of gas, while X-ray observations highlight the energetic particles accelerated by the pulsar.")
image_comparison(
    img1="images/Crab Nebula Hubble.png",
    img2="images/Crab Nebula Chandra.png",
    label1="Hubble",
    label2="Chandra",
)

st.markdown("### Galactic Center")
st.write("The Galactic Center is the dynamic core of the Milky Way, containing the supermassive black hole Sagittarius A*. This composite combines observations from multiple telescopes: Spitzer (infrared), Hubble (near-infrared), and Chandra (X-ray), to reveal both stars and high-energy activity.")
image_comparison(
    img1="https://assets.science.nasa.gov/dynamicimage/assets/science/missions/webb/science/2021/10/STScI-01FJHRV52QBDC4NGBX0K9ZN28A.png?w=2825&h=1645&fit=crop&crop=faces%2Cfocalpoint",
    img2="https://assets.science.nasa.gov/dynamicimage/assets/science/missions/webb/science/2021/10/STScI-01FJHR65YKDTY77QX4CG7HENNP.png?w=2825&h=1645&fit=crop&crop=faces%2Cfocalpoint",
    label1="Hubble",
    label2="Composite",
)

st.markdown("### Sombrero Galaxy")
st.write("The Sombrero Galaxy (M104) is a bright spiral galaxy known for its prominent dust lane and large central bulge. Infrared observations emphasize the structure of dust and cooler material, while optical images highlight its dense star population.")
image_comparison(
    img1="https://esawebb.org/media/archives/images/screen/weic2427d.jpg",
    img2="https://esawebb.org/media/archives/images/screen/weic2427a.jpg",
    label1="Hubble",
    label2="Webb",
)

st.markdown("### M51")
st.write("M51, the Whirlpool Galaxy, is an interacting spiral galaxy with well-defined spiral arms. This comparison shows two Webb instruments: NIRCam (near-infrared) and MIRI (mid-infrared), each revealing different features of dust and star formation.")
image_comparison(
    img1="https://cdn.esawebb.org/archives/images/screen/potm2308b.jpg",
    img2="https://cdn.esawebb.org/archives/images/screen/potm2308d.jpg",
    label1="Webb NIRCam",
    label2="Webb MIRI",
)

st.markdown("### Galaxy Cluster MACS0416")
st.write("MACS0416 is a massive galaxy cluster whose gravity acts as a lens, magnifying distant background galaxies. Infrared observations reveal extremely distant galaxies that are faint or invisible in optical light.")
image_comparison(
    img1="images/MACS0416 Hubble.png",
    img2="images/MACS0416 Webb.png",
    label1="Hubble",
    label2="Webb",
)

st.markdown("### Helix Nebula")
st.write('The Helix Nebula (NGC 7293) is a nearby planetary nebula formed from a dying Sun-like star. Infrared observations reveal dusty structures and comet-like knots extending beyond the bright optical shell.')
image_comparison(
    img1="images/Helix Nebula Hubble.png",
    img2="images/Helix Nebula Webb.png",
    label1="Hubble",
    label2="Webb",
)

st.markdown("### Southern Nebula")
st.write("The Southern Ring Nebula (NGC 3132) is a planetary nebula created by a dying star shedding its outer layers. Infrared imaging reveals a second hidden star and intricate dust structures not easily seen in optical wavelengths.")
image_comparison(
    img1="https://www.webbcompare.com/img/hubble/southern_nebula_700.jpg",
    img2="https://www.webbcompare.com/img/webb/southern_nebula_700.jpg",
    label1="Hubble",
    label2="Webb",
)

st.markdown("### Galaxy Cluster SMACS 0723")
st.write("SMACS 0723 is a distant galaxy cluster whose immense gravity magnifies even more distant galaxies behind it. The deep-field image combines multiple long exposures to reveal thousands of galaxies across cosmic time. This was JWST's first public image in July 2022.")
image_comparison(
    img1="https://www.webbcompare.com/img/hubble/deep_field_700.jpg",
    img2="https://www.webbcompare.com/img/webb/deep_field_700.jpg",
    label1="Hubble",
    label2="Webb",
)

st.markdown("### Carina Nebula")
st.write("The Carina Nebula is a vast star-forming region containing massive young stars that shape the surrounding gas and dust. Infrared observations penetrate thick dust clouds to reveal newborn stars and complex structures.")
image_comparison(
    img1="https://www.webbcompare.com/img/hubble/carina_2800.png",
    img2="https://www.webbcompare.com/img/webb/carina_2800.jpg",
    label1="Hubble",
    label2="Webb",
)

st.markdown("### Stephan's Quintet")
st.write("Stephan's Quintet is a compact group of interacting galaxies undergoing gravitational interactions and shock waves. Infrared observations highlight warm dust and star formation triggered by these galactic collisions.")
image_comparison(
    img1="https://www.webbcompare.com/img/hubble/stephans_quintet_2800.jpg",
    img2="https://www.webbcompare.com/img/webb/stephans_quintet_2800.jpg",
    label1="Hubble",
    label2="Webb",
)

st.markdown("### Tarantula Galaxy")
st.write("The Tarantula Nebula (30 Doradus) is the most active star-forming region in the Local Group of galaxies. Infrared imaging reveals deeply embedded young stars and intricate filamentary structures within the nebula.")
image_comparison(
    img1="https://github.com/JohnEdChristensen/WebbCompare/blob/gh-pages/img/hubble/tarantula_2800.png?raw=true",
    img2="https://github.com/JohnEdChristensen/WebbCompare/blob/gh-pages/img/webb/tarantula_2800.png?raw=true",
    label1="Hubble",
    label2="Webb",
)