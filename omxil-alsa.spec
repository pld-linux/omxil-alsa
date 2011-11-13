Summary:	ALSA Source and Sink audio component for Bellagio OpenMAX IL
Summary(pl.UTF-8):	Komponent audio ALSA Source and Sink dla implementacji Bellagio OpenMAX IL
Name:		omxil-alsa
Version:	0.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/omxil/libomxalsa-%{version}.tar.gz
# Source0-md5:	39273f12cc916f70b1758244cf8e61c4
URL:		http://omxil.sourceforge.net/
BuildRequires:	alsa-lib-devel >= 1.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libomxil-bellagio-devel >= 0.9
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libomxil-bellagio >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/usr/%{_lib}/bellagio

%description
ALSA Source and Sink component is an audio source and output component
for Bellagio OpenMAX IL that uses the libasound library.

%description -l pl.UTF-8
Komponent ALSA Source and Sink to komponent źródła i wyjścia dźwięku
dla implementacji Bellagio OpenMAX IL, wykorzystujący bibliotekę
libasound.

%prep
%setup -q -n libomxalsa-%{version}

%build
# rebuild for as-needed to work
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libomxalsa.so*
