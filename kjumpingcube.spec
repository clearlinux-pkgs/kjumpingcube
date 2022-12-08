#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kjumpingcube
Version  : 22.12.0
Release  : 47
URL      : https://download.kde.org/stable/release-service/22.12.0/src/kjumpingcube-22.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.12.0/src/kjumpingcube-22.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.12.0/src/kjumpingcube-22.12.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0
Requires: kjumpingcube-bin = %{version}-%{release}
Requires: kjumpingcube-data = %{version}-%{release}
Requires: kjumpingcube-license = %{version}-%{release}
Requires: kjumpingcube-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev

%description
KJumpingCube
Matthias Kiefer <matthias.kiefer@gmx.de>
----------------------------------------------------------------------

%package bin
Summary: bin components for the kjumpingcube package.
Group: Binaries
Requires: kjumpingcube-data = %{version}-%{release}
Requires: kjumpingcube-license = %{version}-%{release}

%description bin
bin components for the kjumpingcube package.


%package data
Summary: data components for the kjumpingcube package.
Group: Data

%description data
data components for the kjumpingcube package.


%package doc
Summary: doc components for the kjumpingcube package.
Group: Documentation

%description doc
doc components for the kjumpingcube package.


%package license
Summary: license components for the kjumpingcube package.
Group: Default

%description license
license components for the kjumpingcube package.


%package locales
Summary: locales components for the kjumpingcube package.
Group: Default

%description locales
locales components for the kjumpingcube package.


%prep
%setup -q -n kjumpingcube-22.12.0
cd %{_builddir}/kjumpingcube-22.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1670532998
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
export SOURCE_DATE_EPOCH=1670532998
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kjumpingcube
cp %{_builddir}/kjumpingcube-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kjumpingcube/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kjumpingcube-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kjumpingcube/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kjumpingcube-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kjumpingcube/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kjumpingcube-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kjumpingcube/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kjumpingcube-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kjumpingcube/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
pushd clr-build
%make_install
popd
%find_lang kjumpingcube

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kjumpingcube

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kjumpingcube.desktop
/usr/share/config.kcfg/kjumpingcube.kcfg
/usr/share/icons/hicolor/128x128/apps/kjumpingcube.png
/usr/share/icons/hicolor/16x16/apps/kjumpingcube.png
/usr/share/icons/hicolor/22x22/apps/kjumpingcube.png
/usr/share/icons/hicolor/32x32/apps/kjumpingcube.png
/usr/share/icons/hicolor/48x48/apps/kjumpingcube.png
/usr/share/icons/hicolor/64x64/apps/kjumpingcube.png
/usr/share/kjumpingcube/pics/default.desktop
/usr/share/kjumpingcube/pics/default.svg
/usr/share/metainfo/org.kde.kjumpingcube.appdata.xml
/usr/share/qlogging-categories5/kjumpingcube.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kjumpingcube/index.cache.bz2
/usr/share/doc/HTML/ca/kjumpingcube/index.docbook
/usr/share/doc/HTML/ca/kjumpingcube/settings.png
/usr/share/doc/HTML/de/kjumpingcube/index.cache.bz2
/usr/share/doc/HTML/de/kjumpingcube/index.docbook
/usr/share/doc/HTML/en/kjumpingcube/index.cache.bz2
/usr/share/doc/HTML/en/kjumpingcube/index.docbook
/usr/share/doc/HTML/en/kjumpingcube/settings.png
/usr/share/doc/HTML/es/kjumpingcube/index.cache.bz2
/usr/share/doc/HTML/es/kjumpingcube/index.docbook
/usr/share/doc/HTML/et/kjumpingcube/index.cache.bz2
/usr/share/doc/HTML/et/kjumpingcube/index.docbook
/usr/share/doc/HTML/fr/kjumpingcube/index.cache.bz2
/usr/share/doc/HTML/fr/kjumpingcube/index.docbook
/usr/share/doc/HTML/it/kjumpingcube/index.cache.bz2
/usr/share/doc/HTML/it/kjumpingcube/index.docbook
/usr/share/doc/HTML/nl/kjumpingcube/index.cache.bz2
/usr/share/doc/HTML/nl/kjumpingcube/index.docbook
/usr/share/doc/HTML/pl/kjumpingcube/index.cache.bz2
/usr/share/doc/HTML/pl/kjumpingcube/index.docbook
/usr/share/doc/HTML/pt/kjumpingcube/index.cache.bz2
/usr/share/doc/HTML/pt/kjumpingcube/index.docbook
/usr/share/doc/HTML/pt_BR/kjumpingcube/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kjumpingcube/index.docbook
/usr/share/doc/HTML/ru/kjumpingcube/index.cache.bz2
/usr/share/doc/HTML/ru/kjumpingcube/index.docbook
/usr/share/doc/HTML/sv/kjumpingcube/index.cache.bz2
/usr/share/doc/HTML/sv/kjumpingcube/index.docbook
/usr/share/doc/HTML/uk/kjumpingcube/index.cache.bz2
/usr/share/doc/HTML/uk/kjumpingcube/index.docbook
/usr/share/doc/HTML/uk/kjumpingcube/settings.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kjumpingcube/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kjumpingcube/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kjumpingcube/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kjumpingcube/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kjumpingcube/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f kjumpingcube.lang
%defattr(-,root,root,-)

