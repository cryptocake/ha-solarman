# ⚡ Solarman Stick Logger

[![Stable](https://img.shields.io/github/release/davidrapan/ha-solarman)](https://github.com/davidrapan/ha-solarman/releases/latest)
[![GitHub Activity](https://img.shields.io/github/commit-activity/y/davidrapan/ha-solarman?label=commits)](https://github.com/davidrapan/ha-solarman/commits/main)
[![License](https://img.shields.io/github/license/davidrapan/ha-solarman)](LICENSE)
[![HACS Supported](https://img.shields.io/badge/HACS-Supported-green)](https://github.com/custom-components/hacs)
[![Community Forum](https://img.shields.io/badge/community-forum-brightgreen.svg)](https://community.home-assistant.io/t/solarman-stick-logger-by-david-rapan)
[![Discussions](https://img.shields.io/badge/community-discussions-brightgreen)](https://github.com/davidrapan/ha-solarman/discussions)
[![Wiki](https://img.shields.io/badge/wiki-8A2BE2)](https://github.com/davidrapan/ha-solarman/wiki)

#### 🠶 Signpost
- [Wiki](https://github.com/davidrapan/ha-solarman/wiki)
- [Automations](https://github.com/davidrapan/ha-solarman/wiki/Automations)
- [Custom Sensors](https://github.com/davidrapan/ha-solarman/wiki/Custom-Sensors)
- [Dashboards](https://github.com/davidrapan/ha-solarman/wiki/Dashboards)
- [Naming Scheme](https://github.com/davidrapan/ha-solarman/wiki/Naming-Scheme)
- [Supported Inverters](https://github.com/davidrapan/ha-solarman/wiki/Supported-Inverters)

> [!NOTE]  
> If you are curious about what's planned next look into [🪧 Milestones](https://github.com/davidrapan/ha-solarman/milestones)  
> Use [💬 Discussions](https://github.com/davidrapan/ha-solarman/discussions) for 🙏 Q&A and 💡 Development Planning, etc. and leave [🚩 Issues](https://github.com/davidrapan/ha-solarman/issues) for 🐞 bug reporting, 🎁 feature requests and such...  
> It's still 🚧 work in progress but currently very 🐎 stable 😉  
> *I mean at least for my device as I'm not able to* 🧪 *test it for any other so any* 🧍 *volunteers?* 😊  

> [!IMPORTANT]  
> Inspired by [StephanJoubert/home_assistant_solarman](https://github.com/StephanJoubert/home_assistant_solarman) but w/ a lot of [✍ crucial changes & new features](https://github.com/davidrapan/ha-solarman/wiki#-changes)  
> Implemented using asynchronous [pysolarmanv5](https://github.com/jmccrohan/pysolarmanv5) and fetching through DataUpdateCoordinator + incorporates many more fixes and improvements and also up to date features of HA (while trying to fully preserve backward compatibility)

> [!WARNING]  
> It's not possible to use this integration side by side (with the same device) with the implementation from Stephan! It will override it.  

## 🔨 Installation

[![🔌 Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=davidrapan&repository=ha-solarman&category=integration)

### 🪛 HACS (Manually)
- Follow the link [here](https://hacs.xyz/docs/faq/custom_repositories/)
- Add custom repository: https://github.com/davidrapan/ha-solarman
- Select type of the category: integration
- Find newly added Solarman, open it and then click on the DOWNLOAD button

### 🔧 Manually
- Copy the contents of 'custom_components/solarman' directory into the Home Assistant with exactly the same hirearchy within the '/config' directory

## 👤 Contributors
<a href="https://github.com/davidrapan/ha-solarman/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=davidrapan/ha-solarman" />
</a>
