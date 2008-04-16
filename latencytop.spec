
%define name	latencytop
%define version	0.3
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

%description
LatencyTOP is a Linux tool for software developers (both kernel and
userspace), aimed at identifying where system latency occurs, and
what kind of operation/action is causing the latency to happen. By
identifying this, developers can then change the code to avoid the
worst latency hiccups.

%prep
%setup -q
sed -i 's|-O0|%{optflags} -I%{_includedir}/ncursesw|' Makefile
sed -i 's|"latencytop.trans"|"%{_datadir}/%{name}/latencytop.trans"|' latencytop.c

%build
%make

%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}%{_bindir}
install -d -m755 %{buildroot}%{_datadir}/%{name}
install -m755 %{name} %{buildroot}%{_bindir}
install -m644 latencytop.trans %{buildroot}%{_datadir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/%{name}
