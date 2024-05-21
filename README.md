<!-- markdownlint-disable -->
<p align="center">
    <a href="https://github.com/MonitoringToolbox/">
        <img src="https://cdn.wolfsoftware.com/assets/images/github/organisations/monitoringtoolbox/black-and-white-circle-256.png" alt="MonitoringToolbox logo" />
    </a>
    <br />
    <a href="https://github.com/MonitoringToolbox/nagios-plugin-python-templates/actions/workflows/cicd.yml">
        <img src="https://img.shields.io/github/actions/workflow/status/MonitoringToolbox/nagios-plugin-python-templates/cicd.yml?branch=master&label=build%20status&style=for-the-badge" alt="Github Build Status" />
    </a>
    <a href="https://github.com/MonitoringToolbox/nagios-plugin-python-templates/blob/master/LICENSE.md">
        <img src="https://img.shields.io/github/license/MonitoringToolbox/nagios-plugin-python-templates?color=blue&label=License&style=for-the-badge" alt="License">
    </a>
    <a href="https://github.com/MonitoringToolbox/nagios-plugin-python-templates">
        <img src="https://img.shields.io/github/created-at/MonitoringToolbox/nagios-plugin-python-templates?color=blue&label=Created&style=for-the-badge" alt="Created">
    </a>
    <br />
    <a href="https://github.com/MonitoringToolbox/nagios-plugin-python-templates/releases/latest">
        <img src="https://img.shields.io/github/v/release/MonitoringToolbox/nagios-plugin-python-templates?color=blue&label=Latest%20Release&style=for-the-badge" alt="Release">
    </a>
    <a href="https://github.com/MonitoringToolbox/nagios-plugin-python-templates/releases/latest">
        <img src="https://img.shields.io/github/release-date/MonitoringToolbox/nagios-plugin-python-templates?color=blue&label=Released&style=for-the-badge" alt="Released">
    </a>
    <a href="https://github.com/MonitoringToolbox/nagios-plugin-python-templates/releases/latest">
        <img src="https://img.shields.io/github/commits-since/MonitoringToolbox/nagios-plugin-python-templates/latest.svg?color=blue&style=for-the-badge" alt="Commits since release">
    </a>
    <br />
    <a href="https://github.com/MonitoringToolbox/nagios-plugin-python-templates/blob/master/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Code%20of%20Conduct-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/MonitoringToolbox/nagios-plugin-python-templates/blob/master/.github/CONTRIBUTING.md">
        <img src="https://img.shields.io/badge/Contributing-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/MonitoringToolbox/nagios-plugin-python-templates/blob/master/.github/SECURITY.md">
        <img src="https://img.shields.io/badge/Report%20Security%20Concern-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/MonitoringToolbox/nagios-plugin-python-templates/issues">
        <img src="https://img.shields.io/badge/Get%20Support-blue?style=for-the-badge" />
    </a>
</p>

## Background

Wolf Software has been engaged in providing system, network, and security monitoring solutions from the very outset. Our expertise encompasses a wide range of monitoring solutions, including fundamental ones such as [Munin](http://munin-monitoring.org/) and [Nagios](https://www.nagios.org/), as well as sophisticated enterprise-grade solutions like [New Relic](https://newrelic.com/), [Datadog](https://www.datadoghq.com/), and [AppDynamics](https://www.appdynamics.com/). We also possess experience in creating customized monitoring solutions in-house, tailored to specific client requirements.

## Overview

It is a common occurrence for companies to express the need for ready-made enterprise-grade monitoring solutions, asserting that solutions like [Nagios](https://www.nagios.org/) are becoming obsolete due to the significant investment of time and resources required to make it operational, resulting in similar costs as those incurred with off-the-shelf solutions.

The goal of this project, as well as other initiatives within [The Monitoring Toolbox](https://github.com/MonitoringToolbox), is to demonstrate the ease with which plugins can be developed for tools like [Nagios](https://www.nagios.org/) and [Munin](http://munin-monitoring.org/), thereby enhancing their capabilities to a level that is more comparable to the more costly off-the-shelf alternatives.

## How It Works

The provided template scripts aim to offer all the necessary core functionality while being as minimalistic and lightweight as possible.

### Basic

The [basic](src/basic/basic.py) script provides 5 core functions.

1. main - This function is where you add all of the check related code.
2. handle_ok - This function displayed an `OK` prefixed message (if one is supplied) and then exits the script with the required exit code (0).
3. handle_warning - This function displayed a `WARNING` prefixed message (if one is supplied) and then exits the script with the required exit code (1).
4. handle_critical - This function displayed a `CRITICAL` prefixed message (if one is supplied) and then exits the script with the required exit code (2).
5. handle_unknown - This function displayed an `UNKNOWN` prefixed message (if one is supplied) and then exits the script with the required exit code (3).

### Advanced

The [advanced](src/advanced/advanced.py) script provides the same 5 functions as detailed above, along with an extra function.

1. process_arguments - This function processes the command line arguments, does basic error checking and then calls the main function.

### Template Scripts

| Script                               | Purpose                                                  |
| ------------------------------------ | -------------------------------------------------------- |
| [basic](src/basic/basic.py)          | A basic example check using hard coded values.           |
| [advanced](src/advanced/advanced.py) | An advanced example check using command line parameters. |

## Alternate languages

We have replicated the aforementioned templates in various languages, as individuals and organizations often have a particular language preference or choice.

* [Bash](https://github.com/MonitoringToolbox/nagios-plugin-bash-templates)
* [Perl](https://github.com/MonitoringToolbox/nagios-plugin-perl-templates)
* [Powershell](https://github.com/MonitoringToolbox/nagios-plugin-powershell-templates)
* [Ruby](https://github.com/MonitoringToolbox/nagios-plugin-ruby-templates)

> We would be pleased to generate templates in different languages upon request. Furthermore, we welcome individuals to submit pull requests that include additional languages.

<br />
<p align="right"><a href="https://wolfsoftware.com/"><img src="https://img.shields.io/badge/Created%20by%20Wolf%20on%20behalf%20of%20Wolf%20Software-blue?style=for-the-badge" /></a></p>
