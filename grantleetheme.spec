#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : grantleetheme
Version  : 20.12.0
Release  : 29
URL      : https://download.kde.org/stable/release-service/20.12.0/src/grantleetheme-20.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.12.0/src/grantleetheme-20.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.12.0/src/grantleetheme-20.12.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0 LGPL-2.1
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
BuildRequires : qtbase-dev mesa-dev

%description
# GrantleeTheme #
GrantleeTheme library provides a class for loading theme packages containing
set of templates.

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
%setup -q -n grantleetheme-20.12.0
cd %{_builddir}/grantleetheme-20.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607706258
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1607706258
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/grantleetheme
cp %{_builddir}/grantleetheme-20.12.0/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/grantleetheme/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/grantleetheme-20.12.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/grantleetheme/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/grantleetheme-20.12.0/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/grantleetheme/6f1f675aa5f6a2bbaa573b8343044b166be28399
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
/usr/include/KF5/GrantleeTheme/GenericFormatter
/usr/include/KF5/GrantleeTheme/GrantleeKi18nLocalizer
/usr/include/KF5/GrantleeTheme/GrantleeTheme
/usr/include/KF5/GrantleeTheme/GrantleeThemeEngine
/usr/include/KF5/GrantleeTheme/GrantleeThemeManager
/usr/include/KF5/GrantleeTheme/QtResourceTemplateLoader
/usr/include/KF5/grantleetheme/GenericFormatter
/usr/include/KF5/grantleetheme/GrantleeKi18nLocalizer
/usr/include/KF5/grantleetheme/GrantleeTheme
/usr/include/KF5/grantleetheme/GrantleeThemeEngine
/usr/include/KF5/grantleetheme/GrantleeThemeManager
/usr/include/KF5/grantleetheme/QtResourceTemplateLoader
/usr/include/KF5/grantleetheme/genericformatter.h
/usr/include/KF5/grantleetheme/grantleeki18nlocalizer.h
/usr/include/KF5/grantleetheme/grantleetheme.h
/usr/include/KF5/grantleetheme/grantleetheme_export.h
/usr/include/KF5/grantleetheme/grantleethemeengine.h
/usr/include/KF5/grantleetheme/grantleethememanager.h
/usr/include/KF5/grantleetheme/qtresourcetemplateloader.h
/usr/include/KF5/grantleetheme_version.h
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
/usr/lib64/libKF5GrantleeTheme.so.5.16.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/grantleetheme/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/grantleetheme/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/grantleetheme/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f libgrantleetheme.lang
%defattr(-,root,root,-)

