
%define name	latencytop
%define version	0.5
%define rel	1

Summary:	Visualizer of system latencies
Name:		%name
Version:	%version
Release:	%mkrel %rel
License:	GPLv2
Group:		Development/Other
URL:		http://latencytop.org/
Source:		http://latencytop.org/download/latencytop-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	libncursesw-devel
BuildRequires:	glib2-devel
BuildRequires:  gtk2-devel

%description
LatencyTOP is a Linux tool for software developers (both kernel and
userspace), aimed at identifying where system latency occurs, and
what kind of operation/action is causing the latency to happen. By
identifying this, developers can then change the code to avoid the
worst latency hiccups.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -I%{_includedir}/ncursesw"
%make

%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}%{_sbindir}
%makeinstall_std
install -d -m755 %{buildroot}%{_mandir}/man8
install -m644 latencytop.8 %{buildroot}%{_mandir}/man8/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sbindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man8/latencytop.8*

