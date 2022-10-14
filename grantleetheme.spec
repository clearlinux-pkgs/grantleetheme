#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : grantleetheme
Version  : 22.08.2
Release  : 48
URL      : https://download.kde.org/stable/release-service/22.08.2/src/grantleetheme-22.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.08.2/src/grantleetheme-22.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.08.2/src/grantleetheme-22.08.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 LGPL-2.0 LGPL-2.1
Requires: grantleetheme-data = %{version}-%{release}
Requires: grantleetheme-lib = %{version}-%{release}
Requires: grantleetheme-license = %{version}-%{release}
Requires: grantleetheme-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : grantlee-dev
BuildRequires : kguiaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kiconthemes-dev
BuildRequires : knewstuff-dev

%description
SPDX-License-Identifier: CC0-1.0

%package data
Summary: data components for the grantleetheme package.
Group: Data

%description data
data components for the grantleetheme package.


%package dev
Summary: dev components for the grantleetheme package.
Group: Development
Requires: grantleetheme-lib = %{version}-%{release}
Requires: grantleetheme-data = %{version}-%{release}
Provides: grantleetheme-devel = %{version}-%{release}
Requires: grantleetheme = %{version}-%{release}

%description dev
dev components for the grantleetheme package.


%package lib
Summary: lib components for the grantleetheme package.
Group: Libraries
Requires: grantleetheme-data = %{version}-%{release}
Requires: grantleetheme-license = %{version}-%{release}

%description lib
lib components for the grantleetheme package.


%package license
Summary: license components for the grantleetheme package.
Group: Default

%description license
license components for the grantleetheme package.


%package locales
Summary: locales components for the grantleetheme package.
Group: Default

%description locales
locales components for the grantleetheme package.


%prep
%setup -q -n grantleetheme-22.08.2
cd %{_builddir}/grantleetheme-22.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665717077
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1665717077
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/grantleetheme
cp %{_builddir}/grantleetheme-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/grantleetheme/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9 || :
cp %{_builddir}/grantleetheme-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/grantleetheme/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/grantleetheme-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/grantleetheme/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/grantleetheme-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/grantleetheme/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/grantleetheme-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/grantleetheme/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/grantleetheme-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/grantleetheme/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/grantleetheme-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/grantleetheme/cadc9e08cb956c041f87922de84b9206d9bbffb2 || :
cp %{_builddir}/grantleetheme-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/grantleetheme/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
pushd clr-build
%make_install
popd
%find_lang libgrantleetheme

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/grantleetheme.categories
/usr/share/qlogging-categories5/grantleetheme.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/GrantleeTheme/GrantleeTheme/GenericFormatter
/usr/include/KF5/GrantleeTheme/GrantleeTheme/GrantleeKi18nLocalizer
/usr/include/KF5/GrantleeTheme/GrantleeTheme/GrantleeTheme
/usr/include/KF5/GrantleeTheme/GrantleeTheme/GrantleeThemeEngine
/usr/include/KF5/GrantleeTheme/GrantleeTheme/GrantleeThemeManager
/usr/include/KF5/GrantleeTheme/GrantleeTheme/QtResourceTemplateLoader
/usr/include/KF5/GrantleeTheme/grantleetheme/GenericFormatter
/usr/include/KF5/GrantleeTheme/grantleetheme/GrantleeKi18nLocalizer
/usr/include/KF5/GrantleeTheme/grantleetheme/GrantleeTheme
/usr/include/KF5/GrantleeTheme/grantleetheme/GrantleeThemeEngine
/usr/include/KF5/GrantleeTheme/grantleetheme/GrantleeThemeManager
/usr/include/KF5/GrantleeTheme/grantleetheme/QtResourceTemplateLoader
/usr/include/KF5/GrantleeTheme/grantleetheme/genericformatter.h
/usr/include/KF5/GrantleeTheme/grantleetheme/grantleeki18nlocalizer.h
/usr/include/KF5/GrantleeTheme/grantleetheme/grantleetheme.h
/usr/include/KF5/GrantleeTheme/grantleetheme/grantleetheme_export.h
/usr/include/KF5/GrantleeTheme/grantleetheme/grantleethemeengine.h
/usr/include/KF5/GrantleeTheme/grantleetheme/grantleethememanager.h
/usr/include/KF5/GrantleeTheme/grantleetheme/qtresourcetemplateloader.h
/usr/include/KF5/GrantleeTheme/grantleetheme_version.h
/usr/lib64/cmake/KF5GrantleeTheme/KF5GrantleeThemeConfig.cmake
/usr/lib64/cmake/KF5GrantleeTheme/KF5GrantleeThemeConfigVersion.cmake
/usr/lib64/cmake/KF5GrantleeTheme/KF5GrantleeThemeTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5GrantleeTheme/KF5GrantleeThemeTargets.cmake
/usr/lib64/libKF5GrantleeTheme.so
/usr/lib64/qt5/mkspecs/modules/qt_GrantleeTheme.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/grantlee/5.2/kde_grantlee_plugin.so
/usr/lib64/libKF5GrantleeTheme.so.5
/usr/lib64/libKF5GrantleeTheme.so.5.21.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/grantleetheme/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/grantleetheme/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/grantleetheme/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/grantleetheme/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/grantleetheme/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/grantleetheme/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
/usr/share/package-licenses/grantleetheme/cadc9e08cb956c041f87922de84b9206d9bbffb2
/usr/share/package-licenses/grantleetheme/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f libgrantleetheme.lang
%defattr(-,root,root,-)

