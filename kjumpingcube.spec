#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kjumpingcube
Version  : 19.04.3
Release  : 11
URL      : https://download.kde.org/stable/applications/19.04.3/src/kjumpingcube-19.04.3.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.3/src/kjumpingcube-19.04.3.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.3/src/kjumpingcube-19.04.3.tar.xz.sig
Summary  : A simple tactical game
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kjumpingcube-bin = %{version}-%{release}
Requires: kjumpingcube-data = %{version}-%{release}
Requires: kjumpingcube-license = %{version}-%{release}
Requires: kjumpingcube-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n kjumpingcube-19.04.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1562873363
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1562873363
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kjumpingcube
cp COPYING %{buildroot}/usr/share/package-licenses/kjumpingcube/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/kjumpingcube/COPYING.DOC
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
/usr/share/xdg/kjumpingcube.categories

%files doc
%defattr(0644,root,root,0755)
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
/usr/share/package-licenses/kjumpingcube/COPYING
/usr/share/package-licenses/kjumpingcube/COPYING.DOC

%files locales -f kjumpingcube.lang
%defattr(-,root,root,-)

