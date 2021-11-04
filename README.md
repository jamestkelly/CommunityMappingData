# Community Mapping Data

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#data">Data</a></li>
        <li><a href="#scripting">Scripting</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributors-&-contact-information">Contributors & Contact Information</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This repository houses multiple Python scripts and data used in the project, `Community Mapping`. This repository can be divided into two primary purposes.

* `Data`
* `Scripting`

### Data
The data as contained within the `.data/` directory is used by the `Community Mapping` platform for the rendering of heat-maps for the entirety of Australia on the _Services Profile Page_.

### Scripting
Additionally, several scripts have been developed so as to be able to appropriately convert data as retrieved manually from online sources, i.e. the Australian Bureau of Statistics (ABS), into a singular `geo.json` file. The current file that is utilised for the rendering of heat-maps on the platform is the `geo-numeric.json` file.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

This project has been built with the following tools and technologies.

* [Python](https://www.mapbox.com)

It must be noted that for the best development, [Visual Studio Code](https://code.visualstudio.com) is recommended.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Python
  * With `Homebrew`
    ```sh
    brew install python
    ```

If this does not work, please follow the instructions as available [here](https://www.python.org/downloads/).
### Installation

_The following delineates the process to build and run the scripts locally._

1. Clone the repo
   ```sh
   git clone https://github.com/jamestkelly/CommunityMappingData
   ```
2. For example, to use `UpdateGapScore.py`, ensure that the `geo.json` file you wish to use has had its path updated in the script (the script will always use the latest `.csv` file in the `./data/` directory)
   ```py
   with open('../Data/geo.json') as data_file:
   ```
3. Then, run the script from within the directory, via the terminal
   ```sh
   python3 UpdateGapScore.py
   ```

For access to original source SEIFA data used to generate the `geo.json` files, please refer to [https://www.abs.gov.au/websitedbs/censushome.nsf/home/seifamapping?opendocument&navpos=260](https://www.abs.gov.au/websitedbs/censushome.nsf/home/seifamapping?opendocument&navpos=260).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

The file in the `./data/` directory, `geo-numeric.json` is the current file utilised by the platform `Community Mapping` for the _Services Profile Page_. This file contains the polygons used to generate the heat-map, alongside all data as contained within the `properties` for each region. To update the data used in the mapping of the _Services Profile Page_, please upload the data to an accessible hook, i.e. a public [GitHub](https://github.com) and update the path in the `HeatMap.tsx` file in the `Community Mapping` repository.

```tsx
// Fetch the data globally
useEffect(() => {
    fetch('https://raw.githubusercontent.com/jamestkelly/CommunityMappingData/main/data/geo-numeric.json')
    .then(resp => resp.json())
    .then(json => setData(json))
});
```

It musted be noted that due to the amount of data each of the `Python` scripts parse, so manual changes must be made to conform the data to a `.json` format. Specifically, for the entirety of Australia the last-most set of properties contains strings instead of numeric values for fields like `sa2ID`, etc. As such, these must be converted to strings within the output file manually so as to have the `Community Mapping` platform interpret the file correctly.

<!-- CONTRIBUTING -->
## Contributors & Contact Information

The contributors to this project are as follows:
* Jim Kelly
  * Email: [jim.kelly@connect.qut.edu.au](jim.kelly@connect.qut.edu.au)
* Isaac Guglielmin
  * Email: [isaac.guglielmin@connect.qut.edu.au](isaac.guglielmin@connect.qut.edu.au)
* Samanatha Swift
  * Email: [sj.swift@connect.qut.edu.au](sj.swift@connect.qut.edu.au)
* Luis Villamizar
  * Email: [luisfernando.villamizarpinilla@connect.qut.edu.au](luisfernando.villamizarpinilla@connect.qut.edu.au)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU General Public License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>
