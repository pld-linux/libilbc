Summary:	iLBC Speech Coder
Summary(pl):	Koder mowy iLBC
Name:		libilbc
Version:	1.0
Release:	1
License:	Global IP Sound v2.0 (requires registration for non-personal use)
Group:		Libraries
Source0:	http://simon.morlat.free.fr/download/1.3.x/source/ilbc-rfc3951.tar.gz
# Source0-md5:	c53bb4f1d7184789ab90d2d33571e78a
Source1:	http://ilbcfreeware.org/documentation/gips_iLBClicense.pdf
# Source1-md5:	71cee7ed8e5d5440a53845e7043c4cb5
URL:		http://ilbcfreeware.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iLBC (internet Low Bitrate Codec) is a FREE speech codec suitable for
robust voice communication over IP. The codec is designed for narrow
band speech and results in a payload bit rate of 13.33 kbps with an
encoding frame length of 30 ms and 15.20 kbps with an encoding length
of 20 ms. The iLBC codec enables graceful speech quality degradation
in the case of lost frames, which occurs in connection with lost or
delayed IP packets.

%description -l pl
iLBC (internet Low Bitrate Codec) to darmowy kodek mowy nadajacy si�
do komunikacji g�osowej po IP. Kodek jest zaprojektowany ograniczonych
��cz, a w efekcie wykorzystuje 13.33 kbit/s przy ramce o d�ugo�ci 30
ms i 15.20 kbit/s przy ramce o d�ugo�ci 20 ms. Kodek iLBC umo�liwia
obni�enie jako�ci mowy w przypadku utraconych ramek, co zdarza si� w
przypadku utraty po��czenia lub op�nionych pakiet�w IP.

%package devel
Summary:	Header files for iLBC library
Summary(pl):	Pliki nag��wkowe biblioteki iLBC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for iLBC library.

%description devel -l pl
Pliki nag��wkowe biblioteki iLBC.

%package static
Summary:	Static iLBC library
Summary(pl):	Statyczna biblioteka iLBC
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static iLBC library.

%description static -l pl
Statyczna biblioteka iLBC.

%prep
%setup -q -n ilbc-rfc3951
cp %{SOURCE1} .

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS *.pdf
%attr(755,root,root) %{_libdir}/libilbc.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libilbc.so
%{_libdir}/libilbc.la
%{_includedir}/ilbc

%files static
%defattr(644,root,root,755)
%{_libdir}/libilbc.a
