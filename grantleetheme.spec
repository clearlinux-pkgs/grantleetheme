#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : grantleetheme
Version  : 18.12.2
Release  : 5
URL      : https://download.kde.org/stable/applications/18.12.2/src/grantleetheme-18.12.2.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.2/src/grantleetheme-18.12.2.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.2/src/grantleetheme-18.12.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: grantleetheme-data = %{version}-%{release}
Requires: grantleetheme-lib = %{version}-%{release}
Requires: grantleetheme-license = %{version}-%{release}
Requires: grantleetheme-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : grantlee-dev
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
%setup -q -n grantleetheme-18.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549860693
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1549860693
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/grantleetheme
cp COPYING %{buildroot}/usr/share/package-licenses/grantleetheme/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/grantleetheme/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang libgrantleetheme

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/xdg/grantleetheme.categories
/usr/share/xdg/grantleetheme.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/GrantleeTheme/GrantleeKi18nLocalizer
/usr/include/KF5/GrantleeTheme/GrantleeTheme
/usr/include/KF5/GrantleeTheme/GrantleeThemeEngine
/usr/include/KF5/GrantleeTheme/GrantleeThemeManager
/usr/include/KF5/GrantleeTheme/QtResourceTemplateLoader
/usr/include/KF5/grantleetheme/GrantleeKi18nLocalizer
/usr/include/KF5/grantleetheme/GrantleeTheme
/usr/include/KF5/grantleetheme/GrantleeThemeEngine
/usr/include/KF5/grantleetheme/GrantleeThemeManager
/usr/include/KF5/grantleetheme/QtResourceTemplateLoader
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
/usr/lib64/grantlee/5.1/kde_grantlee_plugin.so
/usr/lib64/libKF5GrantleeTheme.so.5
/usr/lib64/libKF5GrantleeTheme.so.5.10.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/grantleetheme/COPYING
/usr/share/package-licenses/grantleetheme/COPYING.LIB

%files locales -f libgrantleetheme.lang
%defattr(-,root,root,-)

