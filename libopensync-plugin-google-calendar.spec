%define svn 3218

Summary:	OpenSync plugin for Google Calendar
Name:		libopensync-plugin-google-calendar
Version:	0.22.1
Epoch:		1
Release:	0.%{svn}.5
License:	GPLv2+
Group:		Office
Url:		http://www.opensync.org
# For SVN:
# svn co http://svn.opensync.org/branches/branch-0.2X/plugins/google-calendar libopensync-plugin-google-calendar
Source0:	http://www.opensync.org/download/releases/%{name}-%{svn}.tar.lzma
BuildRequires:	pkgconfig(opensync-1.0) < 0.30
BuildRequires:	python-httplib2
Requires:	python-httplib2
Requires:	python-pyxml
Requires:	libopensync >= %{epoch}:0.22

%description
This plugin allows applications using OpenSync to synchronise with Google
Calendar.

%files
%doc README
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*
%{_libdir}/opensync/google-cal-helper

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}

%build
autoreconf -i
# google-cal-helper is installed to libexecdir, we don't want it just
# in /usr/lib... - AdamW 2008/03
%configure2_5x --libexecdir=%{_libdir}/opensync
%make

%install
%makeinstall_std

