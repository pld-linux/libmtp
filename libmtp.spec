Summary:	Implementation of Microsoft's Media Transfer Protocol (MTP)
Summary(pl):	Implementacja protoko³u MTP (Media Transfer Protocol) Microsoftu
Name:		libmtp
Version:	0.0.15
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/libmtp/%{name}-%{version}.tar.gz
# Source0-md5:	5d22b16cb7e6a117cdf489669821df09
URL:		http://libmtp.sourceforge.net/
BuildRequires:	automake
BuildRequires:	libusb-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmtp is an implementation of Microsoft's Media Transfer Protocol
(MTP) in the form of a library suitable primarily for POSIX compliant
operating systems.

%description -l pl
libmtp to implementacja protoko³u przesy³ania mediów MTP (Media
Transfer Protocol) Microsoftu w postaci biblioteki nadaj±cej siê
przede wszystkim dla systemów operacyjnych zgodnych z POSIX.

%package devel
Summary:	Header files for mtp library
Summary(pl):	Pliki nag³ówkowe biblioteki mtp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libusb-devel

%description devel
This is the package containing the header files for mtp library.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki mtp.

%package static
Summary:	Static mtp library
Summary(pl):	Statyczna biblioteka mtp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static mtp library.

%description static -l pl
Statyczna biblioteka mtp.

%prep
%setup -q

%build
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
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libmtp.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/html/*
%attr(755,root,root) %{_libdir}/libmtp.so
%{_libdir}/libmtp.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmtp.a
