#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kcolorchooser
Version  : 18.12.3
Release  : 5
URL      : https://download.kde.org/stable/applications/18.12.3/src/kcolorchooser-18.12.3.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.3/src/kcolorchooser-18.12.3.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.3/src/kcolorchooser-18.12.3.tar.xz.sig
Summary  : Color Chooser
Group    : Development/Tools
License  : MIT
Requires: kcolorchooser-bin = %{version}-%{release}
Requires: kcolorchooser-data = %{version}-%{release}
Requires: kcolorchooser-license = %{version}-%{release}
Requires: kcolorchooser-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde

%description
No detailed description available

%package bin
Summary: bin components for the kcolorchooser package.
Group: Binaries
Requires: kcolorchooser-data = %{version}-%{release}
Requires: kcolorchooser-license = %{version}-%{release}

%description bin
bin components for the kcolorchooser package.


%package data
Summary: data components for the kcolorchooser package.
Group: Data

%description data
data components for the kcolorchooser package.


%package license
Summary: license components for the kcolorchooser package.
Group: Default

%description license
license components for the kcolorchooser package.


%package locales
Summary: locales components for the kcolorchooser package.
Group: Default

%description locales
locales components for the kcolorchooser package.


%prep
%setup -q -n kcolorchooser-18.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555324585
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1555324585
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcolorchooser
cp COPYING %{buildroot}/usr/share/package-licenses/kcolorchooser/COPYING
pushd clr-build
%make_install
popd
%find_lang kcolorchooser

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kcolorchooser

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kcolorchooser.desktop
/usr/share/icons/hicolor/16x16/apps/kcolorchooser.png
/usr/share/icons/hicolor/22x22/apps/kcolorchooser.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcolorchooser/COPYING

%files locales -f kcolorchooser.lang
%defattr(-,root,root,-)

