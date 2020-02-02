#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs

Summary:	Implementation of Microsoft's Media Transfer Protocol (MTP)
Summary(pl.UTF-8):	Implementacja protokołu MTP (Media Transfer Protocol) Microsoftu
Name:		libmtp
Version:	1.1.17
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libmtp/%{name}-%{version}.tar.gz
# Source0-md5:	81aea5d3139e5189c2e055ed2c98cd91
URL:		http://libmtp.sourceforge.net/
BuildRequires:	automake
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	libgcrypt-devel
BuildRequires:	libusb-devel >= 1.0.0
BuildRequires:	pkgconfig
Requires:	libusb >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmtp is an implementation of Microsoft's Media Transfer Protocol
(MTP) in the form of a library suitable primarily for POSIX compliant
operating systems.

%description -l pl.UTF-8
libmtp to implementacja protokołu przesyłania mediów MTP (Media
Transfer Protocol) Microsoftu w postaci biblioteki nadającej się
przede wszystkim dla systemów operacyjnych zgodnych z POSIX.

%package devel
Summary:	Header files for mtp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki mtp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgcrypt-devel
Requires:	libusb-devel >= 1.0.0

%description devel
This is the package containing the header files for mtp library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki mtp.

%package static
Summary:	Static mtp library
Summary(pl.UTF-8):	Statyczna biblioteka mtp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static mtp library.

%description static -l pl.UTF-8
Statyczna biblioteka mtp.

%package progs
Summary:	Utilities from mtp library
Summary(pl.UTF-8):	Narzędzia biblioteki mtp
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description progs
This is the package containing utilities from mtp library.

%description progs -l pl.UTF-8
Ten pakiet zawiera narzędzia z biblioteki mtp.

%package -n udev-libmtp
Summary:	UDEV rules for libmtp devices
Summary(pl.UTF-8):	Reguły UDEV dla urządzeń libmtp
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	udev-core

%description -n udev-libmtp
UDEV rules for libmtp devices.

%description -n udev-libmtp -l pl.UTF-8
Reguły UDEV dla urządzeń libmtp.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure \
	%{?with_apidocs:--enable-doxygen} \
	--with-udev=/lib/udev \
	--with-udev-group=audio \
	--with-udev-mode=0660
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	htmldocdir=%{_docdir}/%{name}-devel-%{version} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libmtp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmtp.so.9

%files devel
%defattr(644,root,root,755)
%if %{with apidocs}
%doc %{_docdir}/%{name}-devel-%{version}
%endif
%attr(755,root,root) %{_libdir}/libmtp.so
%{_libdir}/libmtp.la
%{_includedir}/libmtp.h
%{_pkgconfigdir}/libmtp.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmtp.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mtp-*

%files -n udev-libmtp
%defattr(644,root,root,755)
%attr(755,root,root) /lib/udev/mtp-probe
/lib/udev/hwdb.d/69-libmtp.hwdb
/lib/udev/rules.d/69-libmtp.rules
