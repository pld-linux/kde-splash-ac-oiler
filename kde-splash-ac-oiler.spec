
%define		_splash		ac-oiler

Summary:	KDE splash screen
Summary(pl):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	0.2
Release:	1
License:	GPL v2
Group:		X11/Amusements
Source0:	%{_splash}-%{version}.tar.bz2
# Source0-md5:	06fcded5d94faa5193ed29e93dcf54d4
Provides:	kde-splash
Requires:	kdebase-desktop
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"PLD AC Oiler" KDE splash screen.

%description -l pl
Ekran startowy KDE "Naoliwiacz PLD".

%prep
%setup -q -n ac-oiler

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}
install * $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/%{_splash}
