%define svn	3218
%define rel	3
%if %svn
%define release		%mkrel 0.%svn.%rel
%define distname	%name-%svn.tar.lzma
%define dirname		%name
%else
%define release		%mkrel %rel
%define distname	%name-%version.tar.bz2
%define dirname		%name-%version
%endif

Name: 	 	libopensync-plugin-google-calendar
Version: 	0.22.1
Epoch:		1
Release: 	%{release}
Summary: 	OpenSync plugin for Google Calendar
License:	GPLv2+
Group:		Office
URL:		http://www.opensync.org
# For SVN:
# svn co http://svn.opensync.org/branches/branch-0.2X/plugins/google-calendar libopensync-plugin-google-calendar
Source0:	http://www.opensync.org/download/releases/%{distname}
BuildRequires:	libopensync-devel < 0.30
BuildRequires:	python-httplib2
Requires:	python-httplib2
Requires:	python-pyxml
Requires:	libopensync >= %{epoch}:0.22
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This plugin allows applications using OpenSync to synchronise with Google
Calendar.

%prep
%setup -q -n %{dirname}

%build
%if %svn
autoreconf -i
%endif
# google-cal-helper is installed to libexecdir, we don't want it just
# in /usr/lib... - AdamW 2008/03
%configure2_5x --libexecdir=%{_libdir}/opensync
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*
%{_libdir}/opensync/google-cal-helper

