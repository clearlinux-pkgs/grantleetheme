#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v19
# autospec commit: f35655a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : grantleetheme
Version  : 24.08.1
Release  : 78
URL      : https://download.kde.org/stable/release-service/24.08.1/src/grantleetheme-24.08.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.08.1/src/grantleetheme-24.08.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.08.1/src/grantleetheme-24.08.1.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
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
BuildRequires : gnupg
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n grantleetheme-24.08.1
cd %{_builddir}/grantleetheme-24.08.1
pushd ..
cp -a grantleetheme-24.08.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726181353
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6 \
-DGRANTLEE_BUILD_WITH_QT6=ON \
-DQT_REQUIRED_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6 \
-DGRANTLEE_BUILD_WITH_QT6=ON \
-DQT_REQUIRED_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1726181353
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/grantleetheme
cp %{_builddir}/grantleetheme-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/grantleetheme/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/grantleetheme-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/grantleetheme/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/grantleetheme-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/grantleetheme/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/grantleetheme-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/grantleetheme/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/grantleetheme-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/grantleetheme/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/grantleetheme-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/grantleetheme/cadc9e08cb956c041f87922de84b9206d9bbffb2 || :
cp %{_builddir}/grantleetheme-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/grantleetheme/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang libgrantleetheme6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/grantleetheme.categories
/usr/share/qlogging-categories6/grantleetheme.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim6/GrantleeTheme/GrantleeTheme/GenericFormatter
/usr/include/KPim6/GrantleeTheme/GrantleeTheme/GrantleeKi18nLocalizer
/usr/include/KPim6/GrantleeTheme/GrantleeTheme/GrantleeTheme
/usr/include/KPim6/GrantleeTheme/GrantleeTheme/GrantleeThemeEngine
/usr/include/KPim6/GrantleeTheme/GrantleeTheme/GrantleeThemeManager
/usr/include/KPim6/GrantleeTheme/GrantleeTheme/QtResourceTemplateLoader
/usr/include/KPim6/GrantleeTheme/grantleetheme/GenericFormatter
/usr/include/KPim6/GrantleeTheme/grantleetheme/GrantleeKi18nLocalizer
/usr/include/KPim6/GrantleeTheme/grantleetheme/GrantleeTheme
/usr/include/KPim6/GrantleeTheme/grantleetheme/GrantleeThemeEngine
/usr/include/KPim6/GrantleeTheme/grantleetheme/GrantleeThemeManager
/usr/include/KPim6/GrantleeTheme/grantleetheme/QtResourceTemplateLoader
/usr/include/KPim6/GrantleeTheme/grantleetheme/genericformatter.h
/usr/include/KPim6/GrantleeTheme/grantleetheme/grantleeki18nlocalizer.h
/usr/include/KPim6/GrantleeTheme/grantleetheme/grantleetheme.h
/usr/include/KPim6/GrantleeTheme/grantleetheme/grantleetheme_export.h
/usr/include/KPim6/GrantleeTheme/grantleetheme/grantleethemeengine.h
/usr/include/KPim6/GrantleeTheme/grantleetheme/grantleethememanager.h
/usr/include/KPim6/GrantleeTheme/grantleetheme/qtresourcetemplateloader.h
/usr/include/KPim6/GrantleeTheme/grantleetheme_version.h
/usr/lib64/cmake/KPim6GrantleeTheme/KPim6GrantleeThemeConfig.cmake
/usr/lib64/cmake/KPim6GrantleeTheme/KPim6GrantleeThemeConfigVersion.cmake
/usr/lib64/cmake/KPim6GrantleeTheme/KPim6GrantleeThemeTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6GrantleeTheme/KPim6GrantleeThemeTargets.cmake
/usr/lib64/libKPim6GrantleeTheme.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim6GrantleeTheme.so.6.2.1
/V3/usr/lib64/qt6/plugins/kf6/ktexttemplate/kde_grantlee_plugin.so
/usr/lib64/libKPim6GrantleeTheme.so.6
/usr/lib64/libKPim6GrantleeTheme.so.6.2.1
/usr/lib64/qt6/plugins/kf6/ktexttemplate/kde_grantlee_plugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/grantleetheme/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/grantleetheme/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/grantleetheme/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/grantleetheme/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/grantleetheme/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/grantleetheme/cadc9e08cb956c041f87922de84b9206d9bbffb2
/usr/share/package-licenses/grantleetheme/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f libgrantleetheme6.lang
%defattr(-,root,root,-)

