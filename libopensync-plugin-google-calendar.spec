%define name	libopensync-plugin-google-calendar
%define version	0.36
%define release %mkrel 2

Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	OpenSync Plugin for Google Calendar
License:	GPLv2+
Group:		Office
URL:		http://www.opensync.org
Source:		http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	opensync-devel >= 0.20
BuildRequires:	cmake
Requires:	python-httplib2
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This plugin allows applications using OpenSync to synchronise with Google
Calendar.

%prep
%setup -q

%build
%cmake
%make

%install
rm -rf %{buildroot}
cd build
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING
%{_libdir}/opensync-1.0/google-cal-helper
%{_libdir}/opensync-1.0/plugins/*
%{_datadir}/opensync-1.0/defaults/*
%{_datadir}/opensync-1.0/capabilities/*
%{_datadir}/opensync-1.0/descriptions/*


