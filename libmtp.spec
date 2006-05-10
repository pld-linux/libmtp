Summary:	Implementation of Microsoft's Media Transfer Protocol (MTP)
Name:		libmtp
Version:	0.0.4
Release:	1.1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/libmtp/%{name}-%{version}.tar.gz
# Source0-md5:	ed1ebef445055488e7c18fd5b728bc78
URL:		http://libmtp.sourceforge.net/
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmtp is an implementation of Microsoft's Media Transfer Protocol
(MTP) in the form of a library suitable primarily for POSIX compliant
operating systems.

%package devel
Summary:	Header files for mtp library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for mtp library.

%package static
Summary:	Static mtp library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static mtp library.

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
%attr(755,root,root) %{_libdir}/libmtp.so.*.*.*
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmtp.so
%{_libdir}/libmtp.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmtp.a
