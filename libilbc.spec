Summary:	iLBC Speech Coder
#Summary(pl):	-
Name:		libilbc
Version:	1.0
Release:	1
License:	Global IP Sound v2.0 (requires registration for non-personal use)
Group:		Applications
Source0:	http://simon.morlat.free.fr/download/1.3.x/source/ilbc-rfc3951.tar.gz
# Source0-md5:	c53bb4f1d7184789ab90d2d33571e78a
Source1:	http://ilbcfreeware.org/documentation/gips_iLBClicense.pdf
# Source1-md5:	71cee7ed8e5d5440a53845e7043c4cb5
URL:		http://ilbcfreeware.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iLBC (internet Low Bitrate Codec) is a FREE speech codec suitable for
robust voice communication over IP. The codec is designed for narrow band
speech and results in a payload bit rate of 13.33 kbit/s with an encoding
frame length of 30 ms and 15.20 kbps with an encoding length of 20 ms. The
iLBC codec enables graceful speech quality degradation in the case of
lost frames, which occurs in connection with lost or delayed IP packets.

#%description -l pl

%prep
%setup -q -n ilbc-rfc3951
cp %{SOURCE1} .

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cp -f /usr/share/automake/config.sub .
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
%attr(755,root,root) %{_libdir}/*.so*
%{_includedir}/ilbc
